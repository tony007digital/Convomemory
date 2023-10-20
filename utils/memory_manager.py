# utils/memory_manager.py

import pickle

def save_memory(memory, file_path='memory.pkl'):
    with open(file_path, 'wb') as f:
        pickle.dump(memory, f)

def load_memory(file_path='memory.pkl'):
    with open(file_path, 'rb') as f:
        memory = pickle.load(f)
    return memory
