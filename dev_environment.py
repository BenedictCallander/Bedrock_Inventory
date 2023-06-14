import re

def parse_computer_configuration(config_string):
    components = {
        "Name": "",
        "GPU": "",
        "CPU": "",
        "RAM": "",
        "PSU": ""
    }

    # Split the config string into individual components
    parts = config_string.split(" - ")

    # Extract the components and assign them to the dictionary
    for part in parts:
        if part.startswith("Starter Gaming PC"):
            components["Name"] = part
        elif "Nvidia" in part:
            gpu_match = re.search(r'\bGTX (\d+)', part)
            if gpu_match:
                components["GPU"] = gpu_match.group(1)
        elif "Intel" in part:
            cpu_match = re.search(r'\bIntel (.+)', part)
            if cpu_match:
                components["CPU"] = cpu_match.group(1)
        elif "RAM" in part:
            ram_match = re.search(r'(\d+)GB', part)
            if ram_match:
                components["RAM"] = ram_match.group(1)
        elif "PSU" in part:
            components["PSU"] = part

    return components


# Example usage
config_string = "Starter Gaming PC - Nvidia GTX 960 2GB - Intel i3 4170 - 8GB RAM - Bronze PSU"
parsed_config = parse_computer_configuration(config_string)

# Print the parsed components
for key, value in parsed_config.items():
    print(f"{key}: {value}")
