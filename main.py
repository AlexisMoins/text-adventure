from text_adventure.generators.item_generator import ItemGenerator

if __name__ == "__main__":
    item_generator = ItemGenerator("dungeon/Sentient Valley")
    items = item_generator.generate_items(4)
    for item in items:
        print(f'{item}\n')
