<!DOCTYPE html><html lang="en"><head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chat App with Google Login</title>
  <script type="module" src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js"></script>
  <script type="module" src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js"></script>
  <script type="module" src="https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js"></script>
  <style>
    :root {
      --bg-color: #ffffff;
      --text-color: #000000;
      --input-bg: #f0f0f0;
      --message-bg: #e0e0e0;
      --btn-bg: #1e88e5;
      --btn-text: #ffffff;
    }[data-theme="dark"] {
  --bg-color: #121212;
  --text-color: #ffffff;
  --input-bg: #222222;
  --message-bg: #2c2c2c;
  --btn-bg: #1e88e5;
  --btn-text: #ffffff;
}

* {
  box-sizing: border-box;
  font-family: Arial, sans-serif;
}

body {
  margin: 0;
  background-color: var(--bg-color);
  color: var(--text-color);
}

.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

.btn {
  background: var(--btn-bg);
  border: none;
  color: var(--btn-text);
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 18px;
  cursor: pointer;
}

.chat-container {
  display: none;
  flex-direction: column;
  height: 100vh;
  padding: 20px;
}

.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #333;
  border-radius: 10px;
  background-color: var(--input-bg);
}

.message {
  padding: 8px;
  margin-bottom: 10px;
  border-radius: 6px;
  background: var(--message-bg);
}

.chat-input {
  display: flex;
}

.chat-input input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border-radius: 6px;
  border: 1px solid #ccc;
  margin-right: 10px;
  background-color: var(--input-bg);
  color: var(--text-color);
}

.chat-input button {
  background: var(--btn-bg);
  border: none;
  color: var(--btn-text);
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
}

#search {
  margin: 10px 0;
  padding: 10px;
  border-radius: 6px;
  width: 100%;
  border: none;
  background-color: var(--input-bg);
  color: var(--text-color);
}

  </style>
</head><body data-theme="dark">
  <div class="centered" id="login">
    <h1>Welcome to Chat App</h1>
    <button class="btn" id="google-login">Sign in with Google</button>
  </div>  <div class="chat-container" id="chat">
    <div class="chat-header">
      <h2>Chat Room</h2>
      <div>
        <button class="btn" id="toggle-theme">Toggle Theme</button>
        <button class="btn" id="logout">Logout</button>
      </div>
    </div>
    <input type="text" id="search" placeholder="Search messages..." />
    <div class="chat-messages" id="messages"></div>
    <div class="chat-input">
      <input type="text" id="messageInput" placeholder="Type a message" />
      <button id="send">Send</button>
    </div>
  </div>  <script type="module">
    import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js';
    import { getAuth, signInWithPopup, GoogleAuthProvider, signOut, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js';
    import { getFirestore, collection, addDoc, onSnapshot, query, orderBy } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js';

    const firebaseConfig = {
      apiKey: "AIzaSyDMU9MsmNr0OfKDVB0Hyb8KYZElD-NPiC0",
      authDomain: "chatapp-e21b7.firebaseapp.com",
      databaseURL: "https://chatapp-e21b7-default-rtdb.firebaseio.com",
      projectId: "chatapp-e21b7",
      storageBucket: "chatapp-e21b7.firebasestorage.app",
      messagingSenderId: "56407109760",
      appId: "1:56407109760:web:08df47c54221dc4dabf665",
      measurementId: "G-Q5G798ZVT6"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    const db = getFirestore();

    const loginDiv = document.getElementById('login');
    const chatDiv = document.getElementById('chat');
    const loginBtn = document.getElementById('google-login');
    const logoutBtn = document.getElementById('logout');
    const toggleThemeBtn = document.getElementById('toggle-theme');
    const messagesDiv = document.getElementById('messages');
    const messageInput = document.getElementById('messageInput');
    const sendBtn = document.getElementById('send');
    const searchInput = document.getElementById('search');

    let currentUser = null;

    loginBtn.onclick = async () => {
      try {
        const result = await signInWithPopup(auth, provider);
        currentUser = result.user;
      } catch (e) {
        alert(e.message);
      }
    };

    logoutBtn.onclick = async () => {
      await signOut(auth);
    };

    toggleThemeBtn.onclick = () => {
      const body = document.body;
      const current = body.getAttribute('data-theme');
      body.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
    };

    onAuthStateChanged(auth, (user) => {
      if (user) {
        currentUser = user;
        loginDiv.style.display = 'none';
        chatDiv.style.display = 'flex';
        initChat();
      } else {
        currentUser = null;
        loginDiv.style.display = 'flex';
        chatDiv.style.display = 'none';
      }
    });

    const initChat = () => {
      const q = query(collection(db, 'messages'), orderBy('timestamp'));
      onSnapshot(q, (snapshot) => {
        messagesDiv.innerHTML = '';
        snapshot.docs.forEach(doc => {
          const data = doc.data();
          const msg = document.createElement('div');
          msg.className = 'message';
          msg.textContent = `${data.name}: ${data.text}`;
          messagesDiv.appendChild(msg);
        });
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
      });
    };

    sendBtn.onclick = sendMessage;

    messageInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') sendMessage();
    });

    function sendMessage() {
      const text = messageInput.value.trim();
      if (!text) return;
      addDoc(collection(db, 'messages'), {
        text,
        name: currentUser.displayName,
        uid: currentUser.uid,
        timestamp: Date.now()
      });
      messageInput.value = '';
    }

    searchInput.addEventListener('input', () => {
      const term = searchInput.value.toLowerCase();
      const messages = document.querySelectorAll('.message');
      messages.forEach(msg => {
        msg.style.display = msg.textContent.toLowerCase().includes(term) ? 'block' : 'none';
      });
    });
  </script></body></html>
