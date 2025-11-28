# ==========================================
# ARQUIVO: config.py
# ==========================================
# ATENÇÃO: Este código é PROPOSITALMENTE INSEGURO
# para demonstrar como a pipeline detecta e bloqueia!
# ==========================================

# ------------------------------------------
# PROBLEMA 1: Senha do Banco de Dados Exposta
# ------------------------------------------
DATABASE_CONFIG = {
    "host": "localhost",          # OK - endereço do servidor
    "user": "admin",              # OK - nome de usuário
    "password": "senha123456",    # PROBLEMA! Senha exposta no código
    "database": "producao"        # OK - nome do banco
}
# POR QUE É PERIGOSO:
# - Qualquer pessoa com acesso ao código vê a senha
# - Se o código vazar, o banco fica comprometido
# - Hackers podem acessar todos os dados

# ------------------------------------------
# PROBLEMA 2: API Key da Stripe Exposta
# ------------------------------------------
API_KEY = "sk_live_1234567890abcdefghijklmnop"
# PROBLEMA CRÍTICO!
# 
# O QUE É: Token de acesso da Stripe (sistema de pagamentos)
# POR QUE É PERIGOSO:
# - Começa com "sk_live" = chave de PRODUÇÃO real
# - Com essa chave, hackers podem:
#   → Fazer cobranças fraudulentas
#   → Acessar dados de clientes
#   → Roubar informações de cartões de crédito
# 
# O GITLEAKS VAI DETECTAR PORQUE:
# - Tem o padrão "sk_live_" (conhecido da Stripe)
# - Comprimento típico de API key

# ------------------------------------------
# PROBLEMA 3: Secret Key da AWS Exposta
# ------------------------------------------
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# PROBLEMA GRAVÍSSIMO!
#
# O QUE É: Chave secreta da Amazon Web Services
# POR QUE É PERIGOSO:
# - Com essa chave, hackers podem:
#   → Criar servidores na sua conta AWS
#   → Gerar cobranças milionárias
#   → Acessar todos os seus dados na nuvem
#   → Deletar seus serviços
# 
# O GITLEAKS VAI DETECTAR PORQUE:
# - Formato típico de AWS Secret Key
# - Padrão de caracteres conhecido

# ------------------------------------------
# Esta linha é segura (apenas imprime mensagem)
# ------------------------------------------
print("Configurações carregadas")
#  OK - não tem informação sensível


# ==========================================
# O QUE VAI ACONTECER NA PIPELINE:
# ==========================================
#
# 1. Você faz commit deste arquivo
# 2. Pipeline inicia automaticamente
# 3. Gitleaks escaneia o código
# 4. Gitleaks detecta:
#    ├─ "senha123456" → Senha simples
#    ├─ "sk_live_..." → API Key Stripe
#    └─ "wJalrXU..." → AWS Secret Key
# 5. Pipeline PARA COM ERRO 
# 6. Job "Build and Test" NEM EXECUTA
# 7. Você vê relatório mostrando os 3 problemas
#
# RESULTADO: Código bloqueado! Deploy impedido!
# ==========================================
