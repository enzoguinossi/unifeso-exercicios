<?php

$nome = $_POST["nome"];
$dataNasc = new DateTime($_POST["dataNasc"]);
$dataAtual = new DateTime();

$idade = $dataAtual->diff($dataNasc)->y;

echo "Nome: " . $nome . "<br>";
echo "Idade: " . $idade . " anos<br>";

if ($idade >= 18) {
    echo "A pessoa é maior de idade.";
} else {
    echo "A pessoa é menor de idade.";
}

?>