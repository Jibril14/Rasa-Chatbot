# Rasa Chatbot: E-commerce Rasa Chatbot for Laptop Recommendations

![RasaChatbot](https://res.cloudinary.com/webmonc/image/upload/v1729284928/samples/Git%20Readme%20Images/sample_yh0ihi.png)



---

[Source Code: https://github.com/Jibril14/Rasa-Chatbot ](https://github.com/Jibril14/Rasa-Chatbot)

---

## E-commerce Rasa Chatbot for Laptop Recommendations

---

This project involves the development of an intelligent e-commerce chatbot using Rasa that serves as a user assistant for an online laptop store. The chatbot interacts with users to understand their preferences and recommends laptops based on a preference model and price. It queries the website’s database to retrieve the most suitable laptop options in real time.

The chatbot is built using Python and FastAPI to manage API endpoints and facilitate communication between the chatbot and the database. All chat dialogs are stored in a PostgreSQL database for future analysis and improvement of the chatbot's performance.

This project is containerized using Docker, with both the Rasa chatbot and the API server running as Docker images. Docker Compose orchestrates the deployment, ensuring seamless scalability and maintenance.


## Features:

- **Rasa Chatbot: User Assistance & Recommendations**: Goal-oriented and conversational app, Provides personalized laptop recommendations based on user preferences.
- **Custom Actions**: Aid bot to execute, actions eg API calls, database interactions, etc.
- **Natural Language Understanding (NLU)**: Intent Recognition and Entity Extraction
- **FastAPI & Rasa Integration**: Handles interaction between the chatbot and the server using Python’s FastAPI framework.
- **Pydantic**: For data validation and serialization.
- **SQLAlchemy**: Use for connecting with the database, (save chats, query laptops objects)
- **PostgreSQL**:, Relational database management system (RDBMS) for storing Laptop object and dialog session
- **Fully Containerized**: The entire application is packaged using Docker and managed with Docker Compose for easy deployment. 

