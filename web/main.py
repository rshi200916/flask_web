from shopping import create_app

app = create_app("develop")


# @app.route('/')
# def test():
#     return 'hello'
if __name__ == '__main__':
    app.run()


