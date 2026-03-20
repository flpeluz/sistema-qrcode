from flask import Flask, render_template, abort

app = Flask(__name__)

# Aqui você define os destinos dos seus QR Codes.
# 'slug' é o que vai no final da URL (ex: /video-ia)
QR_DESTINOS = {
    'video-ia': {
        'titulo': 'Agentes de IA',
        'subtitulo': 'Demonstração Prática do Sistema',
        'link_youtube': 'https://youtu.be/iyjzw3xq3e8?si=RQx3Aumw33DbHKjT',
        'cor': 'orange' # Cor da borda e botão
    }
}

@app.route('/<slug>')
def landing_page(slug):
    if slug in QR_DESTINOS:
        projeto = QR_DESTINOS[slug]
        return render_template('index.html', projeto=projeto)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)