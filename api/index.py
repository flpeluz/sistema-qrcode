from flask import Flask, render_template, abort, redirect

app = Flask(__name__, template_folder='../templates')

# Dicionário de Projetos (Fácil de expandir depois)
PROJETOS = {
    'agentes-ia': {
        'titulo': 'Agentes de IA para elaboração de Elogios',
        'texto_botao': 'Elaborar Elogio com Gemini',
        'link_acao': 'https://gemini.google.com/gem/111epwEXh3tKSqEQ88IOhAQ94vDT77WVR?usp=sharing',
        'video_id': 'iyjzw3xq3e8',
        'descricao_video': 'Vídeo de orientação de como utilizar o Agente de IA no Gemini para a elaboração do documento no sistema SEI.'
    }
}

@app.route('/')
def home():
    # Redireciona a raiz para o projeto principal do 15°GB
    return redirect('/agentes-ia')

@app.route('/<slug>')
def landing_page(slug):
    if slug in PROJETOS:
        projeto = PROJETOS[slug]
        return render_template('index.html', projeto=projeto)
    return abort(404)

# Importante para a Vercel: o objeto 'app' deve estar exposto no escopo global
# Não usamos app.run() aqui.