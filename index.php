<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!--
    <header>
        <nav>
            <ul>
                <li>INICIO</li>
                <li>NOSOTROS</li>
                <li>ANUNCIOS</li>
                <li>CONTACTO</li>
            </ul>
        </nav>
        <img src="img/insignia.jpg" alt="">
        <h2>Bienvenido a la</h2>
        <h3>I.E.I JOSE GALVEZ</h3>
    </header>
    -->

<body>
    <header>
        <h1>Colegio JOSE GALVEZ</h1>
        <img src="img/insignia.jpg" alt="">
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Acerca de</a></li>
                <li><a href="#">Admisiones</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>
<div class="main">
    <main>
        <section class="item">
            <h2>Bienvenidos</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </section>
        <section class="item">
            <h2>Nuestro Colegio</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </section>
    </main>
</div>

<div id="chat-container">
    <div id="messages"></div>
    <input type="text" id="user-input" placeholder="Escribe tu mensaje aquí...">
    <button id="send-button">Enviar</button>
  </div>

  <script>
    document.getElementById('send-button').addEventListener('click', function() {
      const userInput = document.getElementById('user-input').value;
      if (userInput.trim() === '') return;

      const messages = document.getElementById('messages');
      messages.innerHTML += `<div><strong>Tú:</strong> ${userInput}</div>`;

      fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
      })
      .then(response => response.json())
      .then(data => {
        messages.innerHTML += `<div><strong>Chatbot:</strong> ${data.response}</div>`;
        messages.scrollTop = messages.scrollHeight;
      })
      .catch(error => {
        console.error('Error:', error);
      });

      document.getElementById('user-input').value = '';
    });
  </script>
    <footer>
        <p>&copy; Colegio Ejemplo 2023</p>
    </footer>

    <script src="script.js"></script>

</body>
</html>
</body>
</html>