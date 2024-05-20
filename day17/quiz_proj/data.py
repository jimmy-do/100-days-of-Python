# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {
#         "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
#                 "to eat.",
#         "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

"""
Implementing New Data
"""
question_data = [
    {"type": "multiple", "difficulty": "medium", "category": "Entertainment: "
                                                                                      "Video Games",
                              "question": "Which Dota 1 hero changed gender when ported to Dota 2?",
                              "correct_answer": "Legion Commander",
                              "incorrect_answers": ["Axe", "Keeper of the Light", "Templar Assassin"]
                              },
                             {"type": "multiple", "difficulty": "easy", "category": "General Knowledge",
                              "question": "What is the name of the company in Lethal Company?",
                              "correct_answer": "The Company",
                              "incorrect_answers": ["Planet Scrap Co.", "Lethal Robotics", "Gordian Shipping Co."]},
                             {"type": "multiple", "difficulty": "medium", "category": "Entertainment: Music",
                              "question": "Which of the following bands is Tom DeLonge not a part of?",
                              "correct_answer": "+44",
                              "incorrect_answers": ["Box Car Racer", "Blink-182", "Angels &amp; Airwaves"]},
                             {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
                              "question": "What does &quot;LCD&quot; stand for?",
                              "correct_answer": "Liquid Crystal Display",
                              "incorrect_answers": ["Language Control Design", "Last Common Difference",
                                                    "Long Continuous Design"]},
                             {"type": "multiple", "difficulty": "medium", "category": "History",
                              "question": "Which of the following snipers has the highest amount of confirmed kills?",
                              "correct_answer": "Simo H&auml;yh&auml;",
                              "incorrect_answers": ["Chris Kyle", "Vasily Zaytsev", "Craig Harrison"]},
                             {"type": "multiple", "difficulty": "easy", "category": "Entertainment: Books",
                              "question": "Which famous book is sub-titled &#039;The Modern Prometheus&#039;?",
                              "correct_answer": "Frankenstein",
                              "incorrect_answers": ["Dracula", "The Strange Case of Dr. Jekyll and Mr. Hyde ",
                                                    "The Legend of Sleepy Hollow"]},
                             {"type": "multiple", "difficulty": "medium", "category": "Celebrities",
                              "question": "Which of these people is NOT a part of the Internet comedy group Mega64?",
                              "correct_answer": "Jon Jafari",
                              "incorrect_answers": ["Rocco Botte", "Derrick Acosta", "Shawn Chatfield"]},
                             {"type": "multiple", "difficulty": "hard", "category": "Entertainment: Music",
                              "question": "What is the English title of the vaporwave track &quot;\u30ea\u30b5\u30d5\u30e9\u30f3\u30af420 \/ \u73fe\u4ee3\u306e\u30b3\u30f3\u30d4\u30e5\u30fc&quot; by Macintosh Plus (Vektroid)?",
                              "correct_answer": "Lisa Frank 420 \/ Modern Computing",
                              "incorrect_answers": ["Smoke Weed 420 \/ Everyday", "Make Your Move 420 \/ My Mind",
                                                    "It&#039;s All In Your Head 420 \/ Understand"]},
                             {"type": "boolean", "difficulty": "medium", "category": "Entertainment: Film",
                              "question": "The original ending of &quot;Little Shop Of Horrors&quot; has the plants taking over the world.",
                              "correct_answer": "True", "incorrect_answers": ["False"]},
                             {"type": "multiple", "difficulty": "easy", "category": "Entertainment: Comics",
                              "question": "What is the full first name of the babysitter in Calvin and Hobbes?",
                              "correct_answer": "Rosalyn", "incorrect_answers": ["Rose", "Ruby", "Rachel"]}]
