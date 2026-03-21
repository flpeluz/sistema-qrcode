from flask import Flask, render_template, abort, redirect

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

PROJETOS = {
    'agentes-ia': {
        'titulo': 'Agente de IA - Elogios',
        'subtitulo_agente': 'Crie a síntese com Gemini',
        'links': [
            {
                'texto': 'Link para elaboração de Elogio', 
                'url': 'https://gemini.google.com/gem/111epwEXh3tKSqEQ88IOhAQ94vDT77WVR?usp=sharing'
            },
            # {
            #     'texto': 'Láureas', 
            #     'url': 'https://gemini.google.com/gem/1uC7CxI9ywb-WHAWddMXdNsYw6EZTB2ZI?usp=sharing'
            # }
        ],
        'video_id': 'iyjzw3xq3e8',
        'descricao_video': 'Vídeo de orientação de como utilizar o Agente de IA no Gemini para a elaboração do documento para o sistema SEI.'
    }
}

@app.route('/')
def home():
    return redirect('/agentes-ia')

@app.route('/<slug>')
def landing_page(slug):
    if slug in PROJETOS:
        projeto = PROJETOS[slug]
        return render_template('index.html', projeto=projeto)
    return abort(404)

if __name__ == '__main__':
    app.run(debug=True)