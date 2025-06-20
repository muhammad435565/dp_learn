<?php

// Telegram se data uthao
$update = json_decode(file_get_contents("php://input"), true);

// User ka message aur chat ID
$message = $update["message"]["text"];
$chat_id = $update["message"]["chat"]["id"];

// Bot ka token
$token = "7112951421:AAEGEpHWb3dC0lPyV9qvjjUnWLZN8aw0pMs";

// Agar user ne /start likha
if ($message == "/start") {
    $text = "Hello World!";

    // Message bhejo Telegram ko
    file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=" . urlencode($text));
}
