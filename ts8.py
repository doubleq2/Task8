# from flask import Flask, jsonify, render_template
from ts6 import *
from fastapi import FastAPI

s = starter("dan")
base = s

app = FastAPI()

baselist2 = []
count = 0
for i,k in base.items():
    a = list(base.items())[count]
    dic = {}
    dic[a[0]] = a[1]
    baselist2.append(dic)
    count+=1
    
# baselist2 это список со словарем base, в котором расположены гонщики с их временем как(ключ:значение),также base это осортированный словарь по времени от малого к большему

for i in range(len(baselist2)):
    baselist2[i]["id"]= i+1
    
# это создает id для каждого гонщика. id = его место в таблице

# def reverse(x):
#     items = list(x.items())
#     y = {k: v for k, v in reversed(items)}
#     return y

# @app.route("/")
# def nach():
#     return "Это ответ на 7 таск (начальная страница)"
        
# @app.route("/report")
# def table():
#     return render_template("table.html",tables=s)

# @app.route("/report/drivers")
# def drivers():
#     return render_template("drivers.html",tables=s)

# @app.route('/report/drivers/driver_id=<string:about>')
# def about(about:str):
#     return render_template("dn.html",dn=about,tables=s)

# @app.route("/report/drivers/order=desc")
# def order():
#     return render_template("table_ord.html",tables=reverse(s))


    
@app.get("/spec/format=json/{id}")
def get_list(id):
    if id == "all":
        return baselist2
    else:
        return baselist2[int(id)-1]

    # @app.route("/spec/format=json",methods=['POST'])
    # def update_list():
    #     new_one = request.json
    #     baselist2.append(new_one)
    #     return jsonify(baselist2)

    # @app.route('/spec/format=json/<int:baselist_id>',methods=['PUT'])
    # def update_spec(baselist_id):
    #     item = next((x for x in baselist2 if x["id"] == baselist_id), None)
    #     params = request.json
    #     if not item:
    #         return {"mess":"No id"}, 400
    #     item.update(params)
    #     return item

    # @app.route('/spec/format=json/<int:baselist_id>',methods=['DELETE'])
    # def delete_spec(baselist_id):
    #     ind, _ = next((x for x in enumerate(baselist2) if x[1]["id"] == baselist_id), (None, None))
    #     baselist2.pop(ind)
    #     return "", 204