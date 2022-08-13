from cgitb import text
from flask import Flask, redirect, url_for
from flask import render_template
from flask import Response, request
from flask import jsonify
import json
import re

app = Flask(__name__)

textbooks = {
    '1':{
        "id": 1,
        "class_id": "COMS W1004",
        "class_name": "Intro to CS and Prog in Java",
        "required_reading": "Yes",
        "professors": ["Paul Blaer", " Adam Cannon"],
        "class_level": ["COMS W1XXX"],
        "title":  "Big Java: Early Objects, 6th Edition",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/61tISWd1egL._SX397_BO1,204,203,200_.jpg",

        "description": "Cay Horstmann's sixth edition of Big Java, Early Objects provides an approachable introduction to fundamental programming techniques and design skills, helping students master basic concepts and become competent coders. Updates for the Java 8 software release and additional visual design elements make this student-friendly text even more engaging. The text is known for its realistic programming examples, great quantity and variety of homework assignments, and programming exercises that build student problem-solving abilities. This edition now includes problem solving sections, more example code online, and exercise from Science and Business.",

        "primaryauthor": ["Horstmann, Cay S."],
        "rating": 5,
        "authors": [{
            "lf": "Horstmann, Cay S.",
            "fl": "Cay S. Horstmann",
            "role": "Author"
        }],
        "asin": "B01AKSZ8XA",
        "isbn_13": "978-1119056447",
        "isbn_10": "1119056446",
        "publication": "Wiley (2016), Edition: 6, 1040 pages",
        "date": "2015",
        "tags": ["Computer Science", "Intro to Java"],
        "language": ["English"],
        "link": "https://www.amazon.com/Big-Java-Early-Objects-6th-ebook/dp/B01AKSZ8XA"
    },
    '2':{
        "id": 2,
        "class_id": "COMS W3134",
        "class_name": "Data Structures in Java",
        "required_reading": "Yes",
        "professors": ["Paul Blaer", " Adam Cannon", " Daniel Bauer"],
        "class_level": ["COMS W3XXX"],
        "title":  "Data Structures and Algorithm Analysis in Java",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/41MMd73GzcL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg",

        "description": "Data Structures and Algorithm Analysis in Java is an “advanced algorithms” book that fits between traditional CS2 and Algorithms Analysis courses. In the old ACM Curriculum Guidelines, this course was known as CS7.This text is for readers who want to learn good programming and algorithm analysis skills simultaneously so that they can develop such programs with the maximum amount of efficiency. Readers should have some knowledge of intermediate programming, including topics as object-based programming and recursion, and some background in discrete math.",

        "primaryauthor": ["Weiss, Mark A."],
        "rating": 5,
        "authors": [{
            "lf": "Weiss, Mark A.",
            "fl": "Mark A. Weiss",
            "role": "Author"
        }],
        "asin": "B006Y14OD8",
        "isbn_13": "978-0132576277",
        "isbn_10": "0132576279",
        "publication": "Pearson (2011), Edition: 3, 648 pages",
        "date": "2011",
        "tags": ["Computer Science", "Intro to Data Structures"],
        "language": ["English"],
        "link": "https://www.amazon.com/Data-Structures-Algorithm-Analysis-Java-ebook/dp/B006Y14OD8"
    },
    '3':{"id": 3,
        "class_id": "COMS W3157",
        "class_name": "Advanced Programing",
        "required_reading": "Yes",
        "professors": ["Jae Lee"],
        "class_level": ["COMS W3XXX"],
        "title": "C Programming Language, 2nd Edition",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/419I0oRkKWL._SX354_BO1,204,203,200_.jpg",

        "description": "The C Programming Language (2nd Ed.). One of the best-selling programming books published in the last fifty years, 'K&R' has been called everything from the 'bible' to 'a landmark in computer science' and it has influenced generations of programmers. Available now for all leading ebook platforms, this concise and beautifully written text is a 'must-have' reference for every serious programmer’s digital library.",

        "primaryauthor": ["Kernighan, Brian W.", "Ritchie, Dennis M.",],
        "rating": 5,
        "authors": [{
            "lf": "Kernighan, Brian W.",
            "fl": "Brian W. Kernighan",
            "role": "Author"
        },
        {
            "lf": "Ritchie, Dennis M.",
            "fl": "Dennis M. Ritchie",
            "role": "Author"
        }],
        "asin": "0131103628",
        "isbn_13": "978-0131103702",
        "isbn_10": "0131103709",
        "publication": "Pearson (1988), Edition: 2, 272 pages",
        "date": "1988",
        "tags": ["Intro to C", "Advanced Programing"],
        "language": ["English"],
        "link": "https://www.amazon.com/C-Programming-Language-2nd-Ed-dp-0131103709/dp/0131103709/ref=mt_other?_encoding=UTF8&me=&qid="
    },

    "4":{
        "id": 4,
        "class_id": "COMS W4701",
        "class_name": "Artificial Intelligence",
        "required_reading": "No",
        "professors": ["Tony Dear", " Ansaf Salleb Aouissi"],
        "class_level": ["COMS W47XX", "COMS 4XXX"],
        "title":  "Artificial Intelligence: A Modern Approach",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/51V7jnPK+7L._SX258_BO1,204,203,200_.jpg",
        "description": "The most comprehensive, up-to-date introduction to the theory and practice of artificial intelligence.The long-anticipated revision of Artificial Intelligence: A Modern Approach explores the full breadth and depth of the field of artificial intelligence (AI). The 4th Edition brings readers up to date on the latest technologies, presents concepts in a more unified manner, and offers new or expanded coverage of machine learning, deep learning, transfer learning, multiagent systems, robotics, natural language processing, causality, probabilistic programming, privacy, fairness, and safe AI. ",
        "primaryauthor": ["Russell, Stuart", "Norvig, Peter"],
        "rating": 5,
        "authors": [{
            "lf": "Russell, Stuart",
            "fl": "Stuart Russell",
            "role": "Author"
        },
        {
            "lf": "Norvig, Peter",
            "fl": "Peter Norvig",
            "role": "Author"
        }],
        "asin": "B092J75GML",
        "isbn_13": "978-0134610993",
        "isbn_10": "0134610997",
        "publication": "Pearson (2021), Edition: 4, 1152  pages",
        "date": "2021",
        "tags": ["Artificial Intelligence","Special Topics", "AI"],
        "language": ["English"],
        "link": "https://www.amazon.com/Artificial-Intelligence-Approach-2-downloads-Artifical-ebook/dp/B092J75GML"
    },
    "5":{
        "id": 5,
        "class_id": "COMS W3157",
        "class_name": "Advanced Programming",
        "required_reading": "Yes",
        "professors": ["Jae Lee"],
        "class_level": ["COMS W3XXX"],
        "title": "A Tour of C++ (C++ In-Depth Series)",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/41k5ZZRFnPL._SX392_BO1,204,203,200_.jpg",
        "description": "In A Tour of C++, Second Edition, Bjarne Stroustrup, the creator of C++, describes what constitutes modern C++. This concise, self-contained guide covers most major language features and the major standard-library components―not, of course, in great depth, but to a level that gives programmers a meaningful overview of the language, some key examples, and practical help in getting started.",
        "primaryauthor": ["Stroustrup, Bjarne"],
        "rating": 5,
        "authors": [{
            "lf": "Stroustrup, Bjarne",
            "fl": "Bjarne Stroustrup",
            "role": "Author"
        }],
        "asin": "0134997832",
        "isbn_13": "978-0134997834",
        "isbn_10": "0134997832",
        "publication": "Addison-Wesley Professional (2018), Edition: 2, 256 pages",
        "date": "2018",
        "tags": ["C++", "Advanced Programming"],
        "language": ["English"],
        "link": "https://www.amazon.com/Tour-2nd-Depth-Bjarne-Stroustrup/dp/0134997832"
    },
    "6":{
        "id": 6,
        "class_id": "COMS W3261",
        "class_name": "Computer Science Theory",
        "required_reading": "Yes",
        "professors": ["Xi Chen", " Mihalis Yannakakis"],
        "class_level": ["COMS W3XXX"],
        "title":  "Introduction to the Theory of Computation",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/41QjHH1OfPL._SX332_BO1,204,203,200_.jpg",

        "description": "Gain a clear understanding of even the most complex, highly theoretical computational theory topics in the approachable presentation found only in the market-leading INTRODUCTION TO THE THEORY OF COMPUTATION, 3E. The number one choice for today's computational theory course, this revision continues the book's well-know, approachable style with timely revisions, additional practice, and more memorable examples in key areas. A new first-of-its-kind theoretical treatment of deterministic context-free languages is ideal for a better understanding of parsing and LR(k) grammars. You gain a solid understanding of the fundamental mathematical properties of computer hardware, software, and applications with a blend of practical and philosophical coverage and mathematical treatments, including advanced theorems and proofs. INTRODUCTION TO THE THEORY OF COMPUTATION, 3E's comprehensive coverage makes this a valuable reference for your continued studies in theoretical computing.",

        "primaryauthor": ["Sipser, Michael"],
        "rating": 5,
        "authors": [{
            "lf": "Sipser, Michael",
            "fl": "Michael Sipser",
            "role": "Author"
        }],
        "asin": "113318779X",
        "isbn_13": "978-1133187790",
        "isbn_10": "113318779X",
        "publication": "Cengage Learning (2012), Edition: 3, 504 pages",
        "date": "2012",
        "tags": ["General Principles",
            "Mathematical (Symbolic) logic", "CS Theory"],
        "language": ["English"],
        "link": "https://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/113318779X"
    },
    "7":{
        "id": 7,
        "class_id": "COMS W4111",
        "class_name": "Introduction to Databases",
        "required_reading": "No",
        "professors": ["Donal Ferguson", " Alexandros Biliris"],
        "class_level": ["COMS W41XX", "COMS W4XXX"],
        "title":  "Database System Concepts",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/51EoEyDdvUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg",

        "description": "ISBN: 9781260084504 is an International Student Edition of Database System Concepts 7th Edition by Abraham Silberschatz, Henry F. Korth, S. Sudarshan This ISBN 9781260084504 is Textbook only. It will not come with online access code. Online Access code (should only be purchased when required by an instructor ) sold separately at other ISBN. The content of of this title on all formats are the same. Database System Concepts by Silberschatz, Korth and Sudarshan is now in its 7th edition and is one of the cornerstone texts of database education. It presents the fundamental concepts of database management in an intuitive manner geared toward allowing students to begin working with databases as quickly as possible. The text is designed for a first course in databases at the junior/senior undergraduate level or the first year graduate level. It also contains additional material that can be used as supplements or as introductory material for an advanced course. Because the authors present concepts as intuitive descriptions, a familiarity with basic data structures, computer organization, and a high-level programming language are the only prerequisites. Important theoretical results are covered, but formal proofs are omitted. In place of proofs, figures and examples are used to suggest why a result is true.",
        
        "primaryauthor": ["Silberschatz, Abraham", "Sudarshan, S.", "Korth, Henry"],
        "rating": 5,
        "authors": [{
            "lf": "Silberschatz, Abraham",
            "fl": "Abraham Silberschatz",
            "role": "Author"
        },
        {
            "lf": "Sudarshan, S.",
            "fl": "S. Sudarshan",
            "role": "Author"
        },
        {
            "lf": "Korth, Henry",
            "fl": "Henry Korth",
            "role": "Author"
        }],
        "asin": "1260084507",
        "isbn_13": "978-1260084504",
        "isbn_10": "1260084507",
        "publication": "McGraw-Hill Education (2019), Edition: 7, 1376 pages",
        "date": "2019",
        "tags": ["data", "security", "Intro to Databases"],
        "language": ["English"],
        "link": "https://www.amazon.com/Database-System-Concepts-Abraham-Silberschatz/dp/1260084507"
    },
    "8":{
        "id": 8,
        "class_id": "COMS W4261",
        "class_name": "Intro to Cryptography",
        "required_reading": "No",
        "professors": ["Tal Malkin"],
        "class_level": ["COMS W4XXX", "others"],
        "title": "Introduction to Cryptography with Coding Theory",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/510NWZHgIkL._SX354_BO1,204,203,200_.jpg",

        "description": "This book assumes a minimal background in programming and a level of math sophistication equivalent to a course in linear algebra. It provides a flexible organization, as each chapter is modular and can be covered in any order. Using Mathematica, Maple, and MATLAB, computer examples included in an Appendix explain how to do computation and demonstrate important concepts. A full chapter on error correcting codes introduces the basic elements of coding theory. Other topics covered: Classical cryptosystems, basic number theory, the data encryption standard, AES: Rijndael, the RSA algorithm, discrete logarithms, digital signatures, e-commerce and digital cash, secret sharing schemes, games, zero knowledge techniques, key establishment protocols, information theory, elliptic curves, error correcting codes, quantum cryptography. For professionals in cryptography and network security.",

        "primaryauthor": ["Trappe, Wade", "Washington, Lawrence"],
        "rating": 5,
        "authors": [{
            "lf": "Trappe, Wade",
            "fl": "Wade Trappe",
            "role": "Author"
        },
        {
            "lf": "Washington, Lawrence",
            "fl": "Lawrence Washington",
            "role": "Author"
        }],
        "asin": "0131862391",
        "isbn_13": "978-0131862395",
        "isbn_10": "0131862391",
        "publication": "Pearson (2005), Edition: 2, 600 pages",
        "date": "2005",
        "tags": ["Computer Science", "Math","Cryptography"],
        "language": ["English"],
        "link": "https://www.amazon.com/Introduction-Cryptography-Coding-Theory-2nd/dp/0131862391"
    },
    "9":{
        "id": 9,
        "class_id": "CSEE W3827",
        "class_name": "Fundamentals of Computer Systems",
        "required_reading": "Yes",
        "professors": ["Daniel Rubenstein", " Martha Kim", " Simha Sethumadhavan"],
        "class_level": ["COMS W3XXX", "CSEE W3XXX", "others"],
        "title": "Logic & Computer Design Fundamentals",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/51vHIFsNukL._SX378_BO1,204,203,200_.jpg",

        "description": "Understanding Logic and Computer Design for All Audiences.Logic and Computer Design Fundamentals is a thoroughly up-to-date text that makes logic design, digital system design, and computer design available to readers of all levels. The Fifth Edition brings this widely recognized source to modern standards by ensuring that all information is relevant and contemporary. The material focuses on industry trends and successfully bridges the gap between the much higher levels of abstraction people in the field must work with today than in the past.",

        "primaryauthor": ["Mano, M. Morris", "Kime, Charles","Martin, Tom"],
        "rating": 5,
        "authors": [{
            "lf": "Mano, M. Morris",
            "fl": "M. Morris Mano",
            "role": "Author"
        },
        {
            "lf": "Kime, Charles",
            "fl": "Charles Kime",
            "role": "Author"
        },
        {
            "lf": "Martin, Tom",
            "fl": "Tom Martin",
            "role": "Author"
        }],
        "asin": "0133760634",
        "isbn_13": "978-0133760637",
        "isbn_10": "0133760634",
        "publication": "Pearson (2015), Edition: 5, 672 pages",
        "date": "2015",
        "tags": ["Circuitry",
            "Computer engineering",
            "Computer Systems"],
        "language": ["English"],
        "link": "https://www.amazon.com/Logic-Computer-Design-Fundamentals-5th/dp/0133760634"
    },

    "10":{
        "id": 10,
        "class_id": "CSEE W3827",
        "class_name": "Fundamentals of Computer Systems",
        "required_reading": "Yes",
        "professors": ["Daniel Rubenstein", " Martha Kim", " Simha Sethumadhavan"],
        "class_level": ["COMS W3XXX", "CSEE W3XXX", "others"],
        "title":  "Computer Organization and Design: The Hardware/Software Interface",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/I/51-FpdiY2HL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg",

        "description": "It covers the revolutionary change from sequential to parallel computing, with a chapter on parallelism and sections in every chapter highlighting parallel hardware and software topics. It includes an appendix by the Chief Scientist and the Director of Architecture of NVIDIA covering the emergence and importance of the modern GPU, describing in detail for the first time the highly parallel, highly multithreaded multiprocessor optimized for visual computing. A companion CD provides a toolkit of simulators and compilers along with tutorials for using them, as well as advanced content for further study and a search utility for finding content on the CD and in the printed text. For the convenience of readers who have purchased an ebook edition or who may have misplaced the CD-ROM, all CD content is available as a download at bit.ly/nFXcLq.",

        "primaryauthor": ["Patterson, David A.", "Hennessy, John L."],
        "rating": 5,
        "authors": [{
            "lf": "Patterson, David A.",
            "fl": "David A. Patterson",
            "role": "Author"
        },
        {
            "lf": "Hennessy, John L.",
            "fl": "John L. Hennessy",
            "role": "Author"
        }],
        "asin": "0123747503",
        "isbn_13": "978-0123747501",
        "isbn_10": "0123747503",
        "publication": "Morgan Kaufmann (2011), Edition: 4, 916 pages",
        "date": "2011",
        "tags": ["Computer Architectures", "Computer Systems"],
        "language": ["English"],
        "link": "https://www.amazon.com/Computer-Organization-Design-Interface-Architecture-ebook/dp/B006FG1HNM"
    }
}

match_title = []

def search_for_substring(textbooks, given_string):
    match_title.clear()
    toreplace = "<span STYLE='color:black; font-weight:bold; background-color: #73dddd;'>\g<0></span>"
    pattern = re.compile(re.escape(given_string), re.I)
    for key, value in textbooks.items():
        # print(given_string)
        # print(value["title"])
        if given_string.lower() in value["title"].lower() or given_string.lower() in value["class_id"].lower() or given_string.lower() in value["class_name"].lower():
            match_title.append({
                "id":value["id"], 
                "title":re.sub(pattern, toreplace,value["title"]),
                "class_id":re.sub(pattern, toreplace,value["class_id"]),
                "class_name": re.sub(pattern, toreplace,value["class_name"]),
                "cover_image": value["cover_image"],
                "professors" :value["professors"]
            })

        #  checking for a match in an array nested inside a dict
        for i  in value["professors"]:
            if given_string.lower() in i.lower():
                new_prof_list = list(filter(lambda prof: i not in prof, value["professors"]))
                new_prof_list.append(" "+re.sub(pattern, toreplace,i))
                match_title.append({
                    "id":value["id"], 
                    "title":re.sub(pattern, toreplace,value["title"]),
                    "class_id":re.sub(pattern, toreplace,value["class_id"]),
                    "class_name": re.sub(pattern, toreplace,value["class_name"]),
                    "cover_image": value["cover_image"],
                    "professors" : new_prof_list
                })

   
    if(len(match_title) == 0):
        pass
    return match_title

def search_by_id(textbooks, id):
    for key, value in textbooks.items():
        if key == str(id):
            return value



# ROUTES

@app.route('/')
def main():
    top_three = [textbooks["1"], textbooks["2"], textbooks["3"]]
    return render_template('main.html', textbooks=top_three)

@app.route('/search/<input_string>')
def search(input_string=None):
    match_items = search_for_substring(textbooks, input_string)

    return render_template('search.html', input_string=input_string, textbooks=textbooks, match_items=match_items)

@app.route('/view/<id>')
def view(id=None):
    view_dict = search_by_id(textbooks, id) 
    title = view_dict["title"]
    cover_image = view_dict["cover_image"]
    description = view_dict["description"]
    author = view_dict["authors"]
    rating = view_dict["rating"]
    link = view_dict["link"]
    tags = view_dict["tags"]
    asin = view_dict["asin"]
    isbn_13 = view_dict["isbn_13"]
    isbn_10 = view_dict["isbn_10"]
    class_id = view_dict["class_id"]
    class_name = view_dict["class_name"]
    required_reading = view_dict["required_reading"]
    professors = view_dict["professors"]
    class_level = view_dict["class_level"]
    
    return render_template('view.html', title=title, cover_image=cover_image, description=description, author=author, rating=rating, link=link, tags=tags, asin=asin, isbn_13=isbn_13, isbn_10=isbn_10, class_id=class_id, class_name=class_name, required_reading=required_reading, professors=professors, class_level = class_level, id=id)

@app.route('/add')
def add():
    return render_template('add.html')


current_id = 10
@app.route('/add_result', methods=['POST', 'GET'])
def add_result():
    global data 
    global current_id 
    
    json_data = request.get_json()
    print("here", json_data)
    title = json_data["title"]
    cover_image = json_data["cover_image"]
    authors = json_data["authors"]
    rating = json_data["rating"]
    description = json_data["description"]
    class_id = json_data["class_id"]
    class_name = json_data["class_name"]
    required_reading = json_data["required_reading"]
    professors = json_data["professors"]
    tags = json_data["tags"]

    # add new entry to array with 
    # a new id and the data the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_textbook_entry = {
        "id": new_id,
        "title": title,
        "cover_image":  cover_image,
        "authors": [{'fl':authors}],
        "rating" : rating,
        "description": description,
        "class_id": class_id,
        "class_name": class_name,
        "required_reading" : required_reading,
        "professors": [professors],
        "tags":[tags],
        "link": "n/a",
        "asin": "n/a",
        "isbn_13": "n/a",
        "isbn_10": "n/a",
        "class_level": ["n/a"]
    }
    textbooks.update({str(new_id): new_textbook_entry})

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(new_data = textbooks[str(new_id)])

@app.route('/edit_data/success/<id>', methods=['POST'])
def add_result_view(id=None):
    if request.method == 'POST':
        edit_data = request.form
        # print(edit_data)
        original_data = search_by_id(textbooks, id) 
        for key, value in textbooks["1"].items():
            if key == "title":
                original_data[key]= edit_data["title"]
            elif key == "cover_image":
                original_data[key] = edit_data["cover_image"]
            elif key == "authors":
                original_data[key] = [{'fl':edit_data["authors"]}]
            elif key == "rating":
                original_data[key] = edit_data["rating"]
            elif key == "description":
                original_data[key] = edit_data["description"]
            elif key == "class_id":
                original_data[key] = edit_data["class_id"]
            elif key == "class_name":
                original_data[key] = edit_data["class_name"]
            elif key == "required_reading":
                original_data[key] = edit_data["required_reading"]
            elif key == "professors": 
                original_data[key] = [edit_data["professors"]]
            elif key == "tags":
                original_data[key] = [edit_data["tags"]]
    return redirect(url_for('view', id=id))

@app.route('/edit/<id>')
def edit(id=None):
    data = search_by_id(textbooks, id) 
    return render_template('edit.html', id=id, data=data)

if __name__ == '__main__':
   app.run(debug = True)
