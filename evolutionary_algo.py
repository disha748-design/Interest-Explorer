import random
from learning_path import hobby_tasks  # Import the hobby tasks


def fitness_function(learning_path, user_profile):
    """
    Fitness function that evaluates a learning path based on the user profile.
    Higher fitness score means better suitability for the user.
    """
    score = 0
    # Reward paths that match the user's skill level with difficulty
    difficulty_gap = abs(learning_path['difficulty'] - user_profile['skill_level'])
    score -= difficulty_gap * 10  # Penalize if the difficulty is not a good match

    # Add score based on how well tasks match user's interests
    unique_tasks = len(set(task['task'] for task in learning_path['tasks']))

    score += unique_tasks * 5  # Reward paths with diverse tasks

    # Optionally, add more weights based on user preferences (creativity, physical activity, etc.)
    if 'creativity' in learning_path.get('tags', []):
        score += user_profile['creativity_level'] * 3  # Example of rewarding creative tasks
    if 'physical_activity' in learning_path.get('tags', []):
        score += user_profile['physical_activity'] * 3

    return score


def generate_random_learning_path(hobby, level):
    """
    Generate a random learning path based on hobby and level.
    """
    available_tasks = hobby_tasks[hobby][level]
    return {
        'tasks': random.sample(available_tasks, k=random.randint(1, min(len(available_tasks), 4))),
        'difficulty': random.uniform(0.5, 1.5),  # Example difficulty score between 0.5 to 1.5
        'tags': ['creativity', 'physical_activity']  # Tags can help to adjust task types
    }


def initialize_population(num_individuals, hobby, level):
    """
    Initialize a population of random individuals (learning paths).
    """
    return [generate_random_learning_path(hobby, level) for _ in range(num_individuals)]


def select_parents_with_elitism(population, user_profile):
    """
    Select parents using fitness function and include elitism (best individual carried over).
    """
    elite = max(population, key=lambda x: fitness_function(x, user_profile))  # Elite individual
    parents = []

    for _ in range(len(population) // 2):  # Pair up individuals
        a, b = random.sample(population, 2)
        parents.append(a if fitness_function(a, user_profile) > fitness_function(b, user_profile) else b)

    parents.append(elite)  # Add the elite to ensure the best individual is carried over

    return parents


def crossover(parent1, parent2, user_profile):
    """
    Crossover two parents to create a child.
    """
    child = {
        'tasks': parent1['tasks'][:len(parent1['tasks']) // 2] + parent2['tasks'][len(parent2['tasks']) // 2:],
        'difficulty': (parent1['difficulty'] + parent2['difficulty']) / 2,
        'tags': parent1['tags'][:1] + parent2['tags'][1:]  # Mix tags from both parents
    }

    # Ensure difficulty is a reasonable match for the user's skill level
    if abs(child['difficulty'] - user_profile['skill_level']) > 0.5:
        child['difficulty'] = random.uniform(user_profile['skill_level'] - 0.5, user_profile['skill_level'] + 0.5)

    return child


def mutate(individual, hobby, level):
    """
    Randomly mutate an individual by swapping out a task with a random one.
    """
    mutation_rate = 0.1
    if random.random() < mutation_rate:
        available_tasks = hobby_tasks[hobby][level]
        individual['tasks'][random.randint(0, len(individual['tasks']) - 1)] = random.choice(available_tasks)


def run_evolutionary_algorithm(user_profile, hobby, level, max_generations=50, population_size=100):
    """
    Run the evolutionary algorithm to generate the best learning path for the user.
    """
    population = initialize_population(population_size, hobby, level)

    for generation in range(max_generations):
        parents = select_parents_with_elitism(population, user_profile)
        offspring = []

        # Generate offspring through crossover
        for i in range(0, len(parents) - 1, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child = crossover(parent1, parent2, user_profile)
            mutate(child, hobby, level)
            offspring.append(child)

        population = parents + offspring

    # Return the best solution (learning path) from the final population
    best_solution = max(population, key=lambda x: fitness_function(x, user_profile))
    return best_solution['tasks']  # Return only the tasks for the best solution
