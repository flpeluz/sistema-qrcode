from flask import Flask, render_template, abort

app = Flask(__name__)

# Aqui é onde você "cadastra" seus novos projetos. 
# Para cada novo QR Code, você adiciona uma linha aqui.
PROJETOS = {
    'agentes-ia': {
        'titulo': 'Agentes de IA',
        'subtitulo': 'Ecossistema Training Track Analytics',
        'link_youtube': 'https://youtu.be/iyjzw3xq3e8?si=RQx3Aumw33DbHKjT',
        'cor': 'orange'
    },
    'logistica': {
        'titulo': 'Logística e PR',
        'subtitulo': 'Gestão de Materiais e Relações Públicas',
        'link_youtube': 'https://www.youtube.com/watch?v=outro_video',
        'cor': 'red'
    }
}

@app.route('/<slug>')
def dynamic_page(slug):
    # Se o link do QR Code (slug) existir no nosso dicionário, ele abre a página
    if slug in PROJETOS:
        dados = PROJETOS[slug]
        return render_template('index.html', projeto=dados)
    else:
        # Se não existir, dá erro 404
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)