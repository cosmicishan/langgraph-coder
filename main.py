from Graphs import graph_builder

def main():
    
    agent = graph_builder()

    response = agent.invoke({"user_prompt": "Develop me a great working Calculator in HTML, CSS and JS. Make sure every functionality is working fine. Make sure there's no bug and everything is working fine."},
                            {"recursion_limit": 10})

    print(response)


if __name__ == "__main__":
    main()
