import asyncio
import random

from enum import Enum, auto
from random import choice


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


neo_reactions = {
    Action.HIGHKICK: Action.HIGHBLOCK,
    Action.LOWKICK: Action.LOWBLOCK,
    Action.HIGHBLOCK: Action.LOWKICK,
    Action.LOWBLOCK: Action.HIGHKICK
}


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)

    async def fight(self):
        neo = Agent()
        self.__aiter__()
        neo.__aiter__()
        while self.health:
            agent_action = await self.__anext__()
            neo_reaction = neo_reactions[agent_action]
            if neo_reaction in (Action.LOWKICK, Action.HIGHKICK):
                self.health -= 1
            print(f"Agent: {agent_action}, Neo: {neo_reaction} Agent Health: {self.health}")
        print('Neo wins!')


async def fightmany(n):
    agents = [Agent().__aiter__() for i in range(n)]
    neo = Agent()
    neo.__aiter__()
    while any(a.health for a in agents):
        alive_agents = [a for a in agents if a.health > 0]
        if not alive_agents:
            break
        agent = random.choice(alive_agents)
        agent_action = await agent.__anext__()
        neo_reaction = neo_reactions[agent_action]
        if neo_reaction in (Action.LOWKICK, Action.HIGHKICK):
            agent.health -= 1
        print(
            f"Agent {agents.index(agent) + 1}: {agent_action}, Neo {neo_reaction}, Agent {agents.index(agent) + 1} "
            f"Health: {agent.health}")
    print('Neo wins!')


if __name__ == "__main__":
    agent = Agent()
    asyncio.run(agent.fight())

    asyncio.run(fightmany(4))
