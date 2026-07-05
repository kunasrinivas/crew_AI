import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import gradio as gr
from crewai import Agent,Task,Crew
from crewai_tools import SerperDevTool

for key in ('SERPER_API_KEY', 'GEMINI_API_KEY'):
    if not os.environ.get(key):
        raise ValueError(f'{key} environment variable is not set')

search_tool = SerperDevTool()

def run_multi_agent(topic):

  teacher = Agent(role= 'Teacher',
                  goal='Explain concepts step by step',
                  backstory = 'Experienced teacher who explain with example',
                  llm = 'gemini-2.5-flash',
                  verbose = True
                  )
  researcher = Agent(role= 'Researcher',
                  goal='Research about concepts which are developing',
                  backstory = 'Expert in searching realworld data',
                  tools=[search_tool],
                  llm = 'gemini-2.5-flash',
                  verbose = True
                  )
  simplifier = Agent(role = 'Simplifier',
                  goal='Make things easy for the students',
                  backstory = 'breaks complex things into simple language',
                  llm = 'gemini-2.5-flash',
                  verbose = True
                  )
  student = Agent(role= 'Student',
                  goal = 'Take Notes',
                  backstory = 'Writes class  notes',
                  llm = 'gemini-2.5-flash',
                  verbose = True)
  examiner = Agent(role= 'Examiner',
                  goal = 'Create Questions',
                  backstory = 'Test Understanding',
                  llm = 'gemini-2.5-flash',
                  verbose = True)

  task1 = Task(
      description=f'Explain {topic} with examples',
      expected_output='give 3 examples',
      agent = teacher,
      verbose = True
  )

  task2 = Task(
      description=f'search and find 3 important points about {topic}',
      expected_output='3 clear poiints',
      agent = researcher,
      verbose = True
  )

  task3 = Task(
      description=f'Explain {topic} in simple language',
      expected_output='make it simpler',
      agent = simplifier,
      verbose = True
  )

  task4 = Task(
      description=f'Create questions for {topic}',
      expected_output='create 3 questions',
      agent = examiner,
      verbose = True
  )
  task5 = Task(
      description=f'Write notes for {topic}',
      expected_output='write notes',
      agent = student,
      verbose = True
  )

  crew = Crew(
      agents=[teacher,researcher,simplifier,student,examiner],
      tasks =[task1,task2,task3,task4,task5],
      verbose=True)

  result = crew.kickoff()

  return str(result)

interface = gr.Interface(
    fn = run_multi_agent,
    inputs = gr.Textbox(
        label = 'Enter Topic',
        placeholder = 'Enter Topic'
        ),
    outputs=gr.Textbox(
        label=' Multi Agent Output'
        ),
    title = 'CrewAI multi Agent AI Workshop',
    description = 'Enter any Topic and see multiple agents collaberate an produce results and test you'
)

if __name__ == '__main__':
  interface.launch()