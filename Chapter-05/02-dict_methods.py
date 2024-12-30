marks = {
    "Rohan": 45,
    "Prakash": 67,
    "Jyoti": 99,
    "Rahul": 78,
    0: "Harry"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Jyoti": "fail"})
# print(marks)
print(marks.get("Jyoti"))
print(marks["Jyoti"])  # if you think both are same then run "Harry" in bracket
# print(marks.get("Harry"))  # Print None
# print(marks["Harry"])  # Returns an error