<?php
$nome = $_POST["nome"];
$dataNasc = new DateTime($_POST["dataNasc"]);
$dataAtual = new DateTime();
$cidade = $_POST["cidade"];
$estadosVisitados = $_POST["estadosVisitados"];

$idade = $dataAtual->diff($dataNasc)->y;

echo "Nome: " . $nome . "<br>";
echo "Idade: " . $idade . " anos<br>";
echo "Cidade: " . $cidade . "<br>";
echo "Estados visitados: " . "<br>";
foreach ($estadosVisitados as $estadoVisitado) {
    echo " - " . $estadoVisitado . "<br>";
}
?>