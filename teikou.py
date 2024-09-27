from flask import Flask, render_template, abort

app = Flask(__name__)

# 各パスに対応するHTMLファイルをマッピング
routes = {
    '/': 'index.html',
    '/index': 'index.html',
    '/index.html': 'index.html',
    '/home': 'index2.html',
    '/home.html': 'index2.html',
    '/math': 'math.html',
    '/math.html': 'math.html',
    '/cookieconsentpolicy': 'cookieconsentpolicy.html',
    '/cookieconsentpolicy.html': 'cookieconsentpolicy.html',
    '/new': 'new.html',
    '/new.html': 'new.html',
    '/play': 'play.html',
    '/play.html': 'play.html',
    '/search': 'search.html',
    '/search.html': 'search.html',
    '/test': 'test.html',
    '/test.html': 'test.html',
    '/settings': 'settings.html',
    '/settings.html': 'settings.html'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:path>')
def serve_page(path):
    # 指定されたパスがroutesに存在するか確認
    if f'/{path}' in routes:
        return render_template(routes[f'/{path}'])
    else:
        return render_template('404.html'), 404  # 404ページを表示

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
