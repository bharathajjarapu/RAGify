import streamlit as st
from embed import EmbeddingHandler
from chunking import TextProcessor
from llm import LLMHandler

class DocumentChat:
    def __init__(self):
        self.embedding_handler = EmbeddingHandler()
        self.text_processor = TextProcessor()
        self.llm_handler = LLMHandler()

    def process_documents(self, pdf_docs):
        """Process documents and create embeddings"""
        # Extract text from PDFs
        raw_text = self.text_processor.get_pdf_text(pdf_docs)
        
        # Create text chunks
        text_chunks = self.text_processor.get_text_chunks(raw_text)
        
        # Create embeddings and add to index
        embeddings = self.embedding_handler.embed_texts(text_chunks)
        self.embedding_handler.add_to_index(embeddings)
        
        return text_chunks

    def get_response(self, query, text_chunks):
        """Get response for a query"""
        # Get similar chunk indices
        similar_indices = self.embedding_handler.search_similar(query)
        
        # Get relevant chunks
        relevant_chunks = [text_chunks[i] for i in similar_indices]
        
        # Generate response
        response = self.llm_handler.generate_response(query, "\n".join(relevant_chunks))
        return response

def main():
    st.title("RAGify")

    # Initialize DocumentChat
    doc_chat = DocumentChat()

    # File upload
    uploaded_files = st.file_uploader(
        "Upload your PDF documents", 
        type=['pdf'], 
        accept_multiple_files=True
    )

    # Initialize session state for text chunks
    if 'text_chunks' not in st.session_state:
        st.session_state.text_chunks = None

    # Process documents when uploaded
    if uploaded_files:
        with st.spinner("Processing documents..."):
            st.session_state.text_chunks = doc_chat.process_documents(uploaded_files)
        st.success("Documents processed successfully!")

    # Chat interface
    if st.session_state.text_chunks is not None:
        user_question = st.text_input("Ask a question about your documents:")

        if user_question:
            with st.spinner("Thinking..."):
                # Generate response
                response = doc_chat.get_response(
                    user_question, 
                    st.session_state.text_chunks
                )
                
                # Display the response
                st.write(response)
    else:
        st.info("Please upload PDF documents to start chatting!")

if __name__ == "__main__":
    main()
