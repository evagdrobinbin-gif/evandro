
# Devolutiva formativa — Atividade 02 da SA

**Estudante:** Evandro  
**Turma:** São Bento do Sul — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** ChocoFactory — Fábrica de chocolate  
**Repositório:** https://github.com/evagdrobinbin-gif/evandro  
**Arquivos observados:** `codigo/app.py` e `interface/index.html`  
**Data da verificação:** 23/11/2026  
**Escopo:** evidências técnicas dos critérios CT6 e CT7, sem atribuição de nota numérica.

## Situação atual do projeto

Foi publicada uma página ChocoFactory com apresentação da fábrica, produtos, processo de produção e contato. O arquivo chamado `codigo/app.py`, porém, contém sintaxe JavaScript (`function`, `const`, `document` e `window`), não código Python. A página utiliza estilos internos e interações simples, sem cadastro ou processamento das operações da fábrica.

## Pontos positivos identificados

- Criou uma página temática com seções de apresentação, catálogo, processo de produção e contato.
- Aplicou HTML estruturado e estilos CSS para cores, layout, produtos e botões.
- Incluiu botão para navegar até os produtos e uma mensagem demonstrativa de contato.
- Criou funções JavaScript para navegação e efeitos de exibição, demonstrando interesse por interatividade.

## O que precisa ser corrigido ou concluído

### 1. Corrigir a linguagem do arquivo `app.py`

O arquivo `.py` contém JavaScript e não poderá ser executado pelo interpretador Python. **Como melhorar:** mover esse conteúdo para `interface/script.js`, ligar o arquivo ao HTML por `<script src="script.js"></script>` e criar em `codigo/app.py` a lógica Python da fábrica.

### 2. Conectar as funções aos elementos da página

O HTML usa ações diretamente nos botões, enquanto parte das funções JavaScript está guardada no arquivo com extensão `.py` e não é carregada pelo navegador. **Como melhorar:** usar funções JS vinculadas a eventos nos botões e testar sua execução.

### 3. Implementar uma funcionalidade do sistema

Os produtos aparecem como conteúdo fixo, sem operação de cadastro, consulta de produção ou cálculo. **Como melhorar:** criar uma atividade simples, como registrar chocolate produzido, quantidade e total, exibindo uma lista ou resumo.

### 4. Separar melhor os arquivos

Os estilos estão dentro do HTML e os arquivos `style.css` e `script.js` do modelo permanecem vazios. **Como melhorar:** mover os estilos para `interface/style.css` e deixar o HTML concentrado na estrutura.

## Oportunidades de melhoria

- Criar funções Python para validar quantidade e registrar produção fictícia.
- Adicionar mensagens específicas para entradas inválidas e confirmação de uma ação.
- Documentar no README a diferença entre o código Python e o JavaScript que opera no navegador.

## Testes recomendados

1. Abrir a página e confirmar a navegação até os produtos.
2. Mover JavaScript para `.js` e verificar se os botões executam suas funções.
3. Criar uma produção com tipo e quantidade válidos.
4. Rejeitar quantidade vazia, negativa ou não numérica.
5. Executar o novo `codigo/app.py` com o interpretador Python.

## Prioridades para a próxima versão

1. **Mover o JavaScript do arquivo `.py` para um arquivo `.js`.**
2. **Criar código Python relacionado à fábrica de chocolate.**
3. **Implementar uma ação funcional com entrada, validação e resultado.**
4. **Separar CSS/JS e atualizar a documentação.**

## Mensagem final

Evandro, a apresentação visual da ChocoFactory é um ponto de partida para a atividade. Agora é importante diferenciar claramente HTML, CSS, JavaScript e Python e concluir pelo menos uma operação que o usuário possa executar e explicar.

