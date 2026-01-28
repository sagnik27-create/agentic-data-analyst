class AgentState:
    def __init__(self, goal):
        self.goal = goal
        self.plan = []
        self.current_step_index = 0
        self.memory = []
        self.retry_count = 0
        self.max_retries = 3
        self.done = False
        self.failed = False
        self.data = None
        self.analysis = None

