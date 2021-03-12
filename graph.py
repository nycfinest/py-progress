# import matplotlib.pyplot as plt


# def square(values):
#     y = []
#     for i in range(len(values)):
#         y.append(values[i] * 2)
#     return y

# x = []
# y = []

# for i in range(100):
#     x.append(i)
    
# y.append(square(x))

# plt.plot(x, y)
# plt.show()


from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

app.run()