def get_current_version():
    with open('fastapi-solcre-core/version.py', 'r') as file:
        version_line = file.readline()
        current_version = version_line.split('=')[1].strip().strip("'")
    return current_version

def increment_version(version):
    parts = version.split('.')
    parts[-1] = str(int(parts[-1]) + 1)  # Incrementa el último componente
    new_version = '.'.join(parts)
    return new_version

def update_version(new_version):
    # Actualizar version.py
    with open('fastapi-solcre-core/version.py', 'w') as file:
        file.write(f"__version__ = '{new_version}'\n")
    
    # Actualizar setup.py
    setup_content = []
    with open('setup.py', 'r') as file:
        for line in file:
            if 'version=' in line:
                setup_content.append(f"    version='{new_version}',\n")
            else:
                setup_content.append(line)
    
    with open('setup.py', 'w') as file:
        file.writelines(setup_content)

if __name__ == "__main__":
    current_version = get_current_version()
    new_version = increment_version(current_version)
    update_version(new_version)
    print(f"Versión actualizada a {new_version}.")
