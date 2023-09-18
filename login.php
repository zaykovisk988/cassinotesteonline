<?php
// Configurações do banco de dados
$servername = "containers-us-west-193.railway.app"; // Endereço do servidor MySQL
$username = "root"; // Nome de usuário do MySQL
$password = "1npAumMVaXN0NIm0lJi7"; // Senha do MySQL
$dbname = "railway"; // Nome do banco de dados
$port = 6698; // Porta do MySQL

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname, $port);


if ($conn->connect_error) {
  die("Conexão falhou: " . $conn->connect_error);
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = $_POST["username"];
  $password = $_POST["password"];

  $sql = "SELECT * FROM users WHERE username = ? AND password = ?";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("ss", $username, $password);
  $stmt->execute();

  $result = $stmt->get_result();
  if ($result->num_rows > 0) {
    echo "Login bem sucedido!";
  } else {
    echo "Nome de usuário ou senha inválidos.";
  }

  $stmt->close();
}

$conn->close();
?>
