import hashlib
import secrets
import os
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass(frozen=True)
class SenhaCriptografada:
    salt: bytes
    hash_bytes: bytes
    _N: int = 2 ** 14
    _R: int = 8
    _P: int = 1

    def verificar(self, senha: str) -> bool:
        hash_verificado = hashlib.scrypt(
            password=senha.encode("utf-8"),
            salt=self.salt,
            n=self._N,
            r=self._R,
            p=self._P,
        )
        return secrets.compare_digest(self.hash_bytes, hash_verificado)

    @staticmethod
    def criar(senha: str) -> 'SenhaCriptografada':
        if len(senha) < 6:
            raise ValueError("A senha deve ter no mínimo 6 caracteres.")

        salt = secrets.token_bytes(16)
        hash_bytes = hashlib.scrypt(
            password=senha.encode("utf-8"),
            salt=salt,
            n=SenhaCriptografada._N,
            r=SenhaCriptografada._R,
            p=SenhaCriptografada._P,
        )
        return SenhaCriptografada(salt=salt, hash_bytes=hash_bytes)

class Usuario:
    def __init__(self, nome: str, senha: str) -> None:
        self.__nome: str = self._tratar_nome(nome)
        self.__senha: SenhaCriptografada = SenhaCriptografada.criar(senha=senha)

    def _tratar_nome(self, nome: str) -> str:
        nome = nome.strip()
        if not nome:
            raise ValueError("Nome não pode ser vazio!")
        return nome.title()

    def autenticar(self, senha: str) -> bool:
        return self.__senha.verificar(senha)

    @property
    def nome(self) -> str:
        return self.__nome

class GerenciadorUsuarios:
    def __init__(self) -> None:
        self.__usuarios: Dict[str, Usuario] = {}

    def cadastrar(self, nome: str, senha: str) -> Usuario:
        nome_busca = nome.strip().lower()
        if nome_busca in self.__usuarios:
            raise ValueError(f"O usuário '{nome}' já existe no sistema.")
        
        novo_usuario = Usuario(nome, senha)
        self.__usuarios[nome_busca] = novo_usuario
        return novo_usuario

    def buscar_por_nome(self, nome: str) -> Optional[Usuario]:
        return self.__usuarios.get(nome.strip().lower())

class AppCLI:
    def __init__(self) -> None:
        self.__gerenciador = GerenciadorUsuarios()

    def _caixa(self, texto: str, largura: int = 40) -> None:
        print("╔" + "═" * largura + "╗")
        print("║" + texto.center(largura) + "║")
        print("╚" + "═" * largura + "╝")

    def _limpar_tela(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def _mostrar_msg(self, msg: str) -> None:
        print(f"\n>>> {msg}")

    def _pausar(self) -> None:
        input("\nPressione Enter para voltar ao menu...")

    def _cadastrar(self) -> None:
        self._limpar_tela()
        self._caixa("CADASTRO DE NOVO USUÁRIO")
        print()
        nome = input("Nome de usuário desejado: ").strip()
        senha = input("Senha (mínimo 6 caracteres): ")
        try:
            usuario = self.__gerenciador.cadastrar(nome, senha)
            self._mostrar_msg(f"Usuário '{usuario.nome}' cadastrado com sucesso!")
        except ValueError as e:
            self._mostrar_msg(f"Erro no cadastro: {e}")
        self._pausar()

    def _login(self) -> None:
        self._limpar_tela()
        self._caixa("ÁREA DE ACESSO")
        print()
        nome = input("Nome de usuário: ").strip()
        senha = input("Sua senha: ")
        
        usuario = self.__gerenciador.buscar_por_nome(nome)
        if usuario and usuario.autenticar(senha):
            self._mostrar_msg(f"Bem-vindo, {usuario.nome}!")
        else:
            self._mostrar_msg("Credenciais inválidas.")
        self._pausar()

    def executar(self) -> None:
        self._limpar_tela()
        while True:
            self._limpar_tela()
            self._caixa("SISTEMA DE LOGIN")
            print("\n[1] Cadastrar Usuário")
            print("[2] Realizar Login")
            print("[0] Sair do Sistema")
            
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                self._cadastrar()
            elif opcao == "2":
                self._login()
            elif opcao == "0":
                self._pausar()
                self._mostrar_msg("Encerrando programa...")
                break
            else:
                self._mostrar_msg("Opção inválida! Tente novamente.")
                self._pausar()

if __name__ == "__main__":
    app = AppCLI()
    app.executar()
