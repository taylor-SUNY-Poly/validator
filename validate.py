def validate_exam_1(exam):
    exam_keys = ["student_name",
            "student_number",
            "exam_id",
            "Q1",
            "Q2",
            "Q3",
            "Q4",
            "Q5",
            "Q6",
            "Q7",
            "Q8",
            "Q9",
            "Q10",
            "Q11",
            "Q12",
            "Q13",
            "Q14",
            "Q15",
            "Q16",
            "Q17",
            "Q18",
            "Q19",
            "Q20",
            "Q21",
            "Q22",
            ]
    valid_exam_ids = ["A191","A242","A373","A404"]
    error_output = ""
    code_trace_default ='''
Replace this text.
And this text.
'''

    for k in exam_keys:
        if not(k in list(exam.keys())):
            error_output += f"{k} not found in exam data\n"
    if error_output != "":
        error_output += "If data is missing you may not have run\nthe code cell that contains this data."
        print(error_output)
    else:
        if exam["student_name"] == "Your Name Here":
            error_output += "You did not record your name!\n"
        if exam["student_number"] == "Your U Number Here":
            error_output += "You did not record your U-number!\n"
        if not(exam["exam_id"] in valid_exam_ids):
            error_output += "You did not record a valid exam id!\n"
    
        ### T/F Validation
        for q in (["Q"+str(x) for x in range(1, 10+1)]):
            if not(exam[q] in ["True", "False"]):
                error_output += f"For {q} your answer is not recorded as True or False\n"
        
        ### MC Validation
        for q in (["Q"+str(x) for x in range(11, 16+1)]):
            if not(exam[q] in ["A", "B", "C", "D"]):
                error_output += f"For {q} your answer is not recorded as A or B or C or D\n"
        
        ### Short Response Validation
        for q in (["Q"+str(x) for x in range(17, 19+1)]):
            if exam[q] == "Replace this text, your answer may take up multiple lines.":
                error_output += f"For {q} your answer has not been saved, re-run the cell"
        
        ### Code Trace Validation
        for q in (["Q"+str(x) for x in range(20, 21+1)]):
            if exam[q] == code_trace_default:
                error_output += f"For {q} your answer has not been saved, re-run the cell"
        
        ### Programming in C Validation (Do not need to complete additional validation)
        if error_output != "":
            print(error_output)
        else:
            print("Validation Complete, no trivial errors in exam data")

if __name__ == "__main__":
    test_exam = {}
    validate_exam_1(test_exam)