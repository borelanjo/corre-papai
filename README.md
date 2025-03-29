
# Corre, Papai! — Um Jogo em Python com Pygame

## Sobre o Projeto

**Corre, Papai!** é um projeto pessoal gamificado que simula a jornada de um pai tentando alcançar sua filha fujona dentro de um labirinto. O jogo é desenvolvido em Python usando a biblioteca **Pygame**, com foco em aprendizado incremental de desenvolvimento de jogos 2D, boas práticas de programação, testes com **TDD**, e até o uso de **IA (ChatGPT)** como parceiro de estudo e criação.

Este projeto tem como objetivo:
- Aprender desenvolvimento de jogos 2D com Python de forma prática e divertida
- Praticar Test-Driven Development (TDD) desde o início
- Explorar Pygame, lógica de movimentação, colisão, animação e IA básica
- Criar algo que possa futuramente ser compartilhado com a filha do autor
- Usar a IA como ferramenta de apoio técnico e criativo ao longo da jornada

---

## Ferramentas e Tecnologias

- **Python** 3.x
- **Pygame**
- **unittest** (para TDD)
- **ChatGPT** (apoio técnico, organização, criatividade)
- **VS Code** (IDE recomendada)
- Planejamento e documentação em **Markdown**

---

## Roadmap Gamificado

### Mundo 1: O Começo do Labirinto
*“Lis fugiu rindo! Hora de sair do sofá e encarar o labirinto.”*
- [ ] Criar o mapa base com paredes e caminhos (matriz ou `.txt`)
- [ ] Mostrar o labirinto na tela com blocos desenhados
- [ ] Controlar o pai com teclas (setas ou WASD)
- [ ] Impedir que ele atravesse paredes
- [ ] Mostrar a posição da filha no mapa  
**Conquista desbloqueada:** `Primeiros passos do papai`

---

### Mundo 2: A Fugitiva
*“Você ouve uma risada no fundo... ela está em movimento!”*
- [ ] Programar a filha correndo automaticamente por caminhos livres
- [ ] Fazer a movimentação dela parecer 'esperta'
- [ ] Adicionar uma mensagem engraçada aleatória enquanto ela corre
- [ ] Testar se ela evita paredes corretamente  
**Conquista desbloqueada:** `Ela não vai escapar pra sempre`

---

### Mundo 3: O Encontro
*“Você a alcança — mas será que é o suficiente?”*
- [ ] Detectar colisão entre pai e filha = vitória
- [ ] Adicionar mensagem de vitória
- [ ] Criar sistema de pontuação  
**Conquista desbloqueada:** `Pai do Ano`

---

### Mundo 4: O Desafio Cresce
*“Ela aprendeu a se esconder... e o tempo está contra você!”*
- [ ] Adicionar temporizador regressivo
- [ ] Criar um ponto secreto de fuga da filha
- [ ] Exibir mensagem de derrota  
**Conquista desbloqueada:** `Desafio real`

---

### Mundo 5: O Labirinto Vivo
*“Cada vez que você joga... o labirinto muda!”*
- [ ] Criar gerador procedural de labirinto simples
- [ ] Adicionar fases com dificuldade crescente
- [ ] Permitir recomeçar a partida com tecla ou botão  
**Conquista desbloqueada:** `Papai profissional`

---

### Mundo Extra: Amor, carinho e risadas
*“Um jogo feito por um pai, com amor e código.”*
- [ ] Adicionar sprites personalizados
- [ ] Criar efeito de abraço (animação)
- [ ] Colocar músicas e efeitos sonoros
- [ ] Adicionar mensagens engraçadas e fofas da filha  
**Conquista desbloqueada:** `Lis vai amar isso um dia`

---

> Este projeto foi pensado para ser divertido, educativo e afetivo — uma forma de unir aprendizado técnico, criatividade e amor de pai.

---

## Como rodar o projeto localmente

### Pré-requisitos
- Python 3.10 ou superior instalado
- `pip` funcionando normalmente
- (Opcional) Criar um ambiente virtual com `venv`

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/corre-papai.git
cd corre-papai

# Crie o ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt
```

### Execução do jogo
```bash
python main.py
```

---

## Como rodar os testes
```bash
# Executar todos os testes com unittest
python -m unittest discover -s tests
```

---

## Organização futura

O projeto está sendo desenvolvido com base em TDD e será organizado por fases (milestones), cada uma com seu conjunto de tarefas e objetivos específicos. Veja os arquivos de milestones para acompanhar o progresso de cada mundo.

> Este projeto é uma jornada de aprendizado e diversão — feito com carinho por um pai programador.
