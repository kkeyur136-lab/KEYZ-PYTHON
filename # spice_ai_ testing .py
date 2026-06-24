# spice_ai.py

def solve_problem():
    problem = input("\n🔍 What's a problem you want to solve? \n> ")
    print("\n✅ Problem Breakdown:")
    print(f"- What do you already know about '{problem}'?")
    print("- What do you need to research more?")
    print("- Who faces this and how does it impact them?")


def prompt_questions():
    topic = input("\n🧠 Enter your topic for creative questioning: \n> ")
    print("\n💡 Here are 3 creative questions:")
    print(f"1. What if {topic} worked underwater or in space?")
    print(f"2. How could kids or elders benefit from {topic}?")
    print(f"3. What would make {topic} exciting for students to use?")


def imagine_ideas():
    base = input("\n🎨 What's your topic or idea base? \n> ")
    print("\n🚀 Wild & Futuristic Ideas:")
    print(f"1. A hologram-based {base} that teaches in 3D.")
    print(f"2. A portable {base} that runs on solar energy.")
    print(f"3. An AI version of {base} that talks in your native language.")


def create_project():
    idea = input("\n🛠️ Which idea do you want to build into a project? \n> ")
    print("\n📦 Project Blueprint:")
    print(f"📌 Name: Project {idea.title()}")
    print(f"💡 What it does: Solves problem using '{idea}' concept.")
    print("📝 Steps to Build:\n - Sketch it\n - List materials\n - Build with tools\n - Test & improve")
    print("🧰 Tools: Python, Arduino, Sensors, Cardboard, App")


def evolve_idea():
    idea = input("\n🔁 What idea/project would you like to improve? \n> ")
    print("\n✨ Idea Upgrades:")
    print(f"- Add AI for smarter results.")
    print(f"- Make it work offline or in low-power areas.")
    print(f"- Add voice or gesture control.")
    print(f"- Expand it to schools, homes, or public places.")


def main():
    print("\n🎓 Welcome to SPICE AI – Student Creative Assistant 🤖")
    while True:
        print("\nSelect a module to run:")
        print("1. Solve a Problem")
        print("2. Ask Creative Questions")
        print("3. Imagine Ideas")
        print("4. Create a Project")
        print("5. Improve an Idea")
        print("6. Exit")

        choice = input("👉 Enter your choice (1-6): ")

        if choice == '1':
            solve_problem()
        elif choice == '2':
            prompt_questions()
        elif choice == '3':
            imagine_ideas()
        elif choice == '4':
            create_project()
        elif choice == '5':
            evolve_idea()
        elif choice == '6':
            print("\n👋 Thanks for using SPICE AI. Keep creating!")
            break
        else:
            print("❌ Invalid choice. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()


###### just testing model #############