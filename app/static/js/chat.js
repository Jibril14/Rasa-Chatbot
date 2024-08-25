const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const shopUi = document.querySelector(".row");
console.log("########ShopUI",shopUi)


let shop
let userMessage = null;
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">
    <img src="https://res.cloudinary.com/webmonc/image/upload/v1696515089/7626850_ppkstm.png" width="24" height="28" alt="bot">
    </span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    console.log("MSG",message)
    return chatLi;
}

const generateResponse = (data) => {
    // display thinking, when response is not there yet
    const chatElement = createChatLi("...thinking", "incoming");
    chatbox.appendChild(chatElement);
    chatbox.scrollTo(0, chatbox.scrollHeight);
    const messageElement = chatElement.querySelector("p");

    messageElement.textContent = data

    chatbox.scrollTo(0, chatbox.scrollHeight);
}

const displayShop = (data) => {
    if(data.length != 0){  
        shop  = document.createElement("div")
        shop.classList.add("col")
        for (const i of data){
            const shop  = document.createElement("div")
            shop.classList.add("col")
            const card =`
                <div id="content">
                    <div class="img-container1">
                        <div class="img-container">
                            <img src="${i.image}"  alt="" >  
                        </div>
                    </div>
                    <h4 id="name">${i.name}</h4>
                    <div class="inner-content">
                        <p>&#36<span id="id">${i.price}</span></p>
                        <button id="idd" class="cart-btn">Add to cart</button>
                    </div>
                </div>`
          shop.innerHTML = card; 
          shopUi.appendChild(shop)
        }
    } else {
        // remove previous elements on ui
        while (shopUi.hasChildNodes()){
            shopUi.removeChild(shopUi.firstChild)
        }
    }  
}

const handleChat = () => {
    userMessage = chatInput.value.trim();
    if(!userMessage) return;

    botResponse = sendMessageToServer(userMessage)
    console.log("Bot Response", botResponse)
    // after user enter message
    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);   
    
}


const sendMessageToServer = (data) => {
    
    // send user message to server
    // const botResponse = "Im coming from Rasa"
    console.log("User message",data)
    return fetch("http://127.0.0.1:8000/message", {
        method: "POST", 
        body: JSON.stringify({

            "chatId": 1,
            "date": "date",
            "conversation": data
        }),
        headers: {
            "Content-type": "application/json"
        }
    }).then(response => {   
        return response.json()
    }).then((data) => {
        console.log("DATA",data)
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(data["message"]);
        console.log("Extras:",data["extra"])
        displayShop(data["extra"])
    }
    ).catch(
        (err) => console.log(err)
    )
}

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window
    // width is greater than 800px, handle the chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault(); // prevent expansion of textarea
        handleChat();
        // const element = document.querySelector(".col")
        
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));