from flask import Flask, render_template, abort

app = Flask(__name__)

# Aqui você define os destinos dos seus QR Codes.
# 'slug' é o que vai no final da URL (ex: /video-ia)
PROJETOS = {
    'agentes-ia': {
        'titulo': 'Agentes de IA para elaboração de Elogios',
        'texto_botao': 'Elaborar Elogio com Gemini',
        'link_acao': 'https://gemini.google.com/gem/111epwEXh3tKSqEQ88IOhAQ94vDT77WVR?usp=sharing', # Link para onde o botão leva
        'video_id': 'iyjzw3xq3e8', # Apenas o código final do seu vídeo
        'descricao_video': 'Vídeo de orientação de como utilizar o Agente de IA no Gemini para a elaboração do documento no sistema SEI.'
    }
}

@app.route('/<slug>')
def landing_page(slug):
    if slug in PROJETOS:
        projeto = PROJETOS[slug]
        return render_template('index.html', projeto=projeto)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)