# /c:/Python314/server_management_console.py

# 1. Module-Level Variable (Global Scope)
SERVERS = {
    "Web_Alpha": "Online",
    "DB_Storage": "Offline",
    "Mail_Relay": "Online"
}

def display_menu():
    """Display the system menu."""
    print("\n========================================")
    print(">>> SYSADMIN MENU <<<")
    print("1. View All Servers")
    print("2. Change Server Status")
    print("3. Add New Server")
    print("4. Exit")
    print("========================================")

def show_status():
    """Display current status of all SERVERS."""
    print("\n--- CURRENT SERVER STATUS ---")
    for name, status in SERVERS.items():
        print(f"[{name}]: {status}")

def update_server(server_name, status="Online"):
    """Update a server's status if it exists."""
    if server_name in SERVERS:
        SERVERS[server_name] = status
        print(f"Task: Setting {server_name} to {status}...")
    else:
        print("Error: Server not found.")

def add_server():
    """Prompt user to add a new server to SERVERS."""
    name = input("Enter new server name: ").strip()
    
    # Optional Safety Check
    if name in SERVERS:
        print("Error: Server already exists.")
        return

    if not name:
        print("No name entered.")
        return

    status = input("Enter initial state: ").strip()
    if not status:
        status = 'Offline'
        
    SERVERS[name] = status
    print(f"Success: Added {name} as {status}.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            show_status()
            
        elif choice == '2':
            # Inputs moved here to match template signature for update_server
            name = input("Which server name?: ").strip()
            new_status = input("Enter new status: ").strip()
            
            if new_status:
                update_server(name, new_status)
            else:
                print("No status entered.")
                
        elif choice == '3':
            add_server()
            
        elif choice == '4':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Entry point of the script
if __name__ == "__main__":
    main()