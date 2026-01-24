// Toggle user dropdown menu
window.toggleUserMenu = function(event) {
    console.log('toggleUserMenu called');
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    const menu = document.getElementById('userMenu');
    console.log('Menu element:', menu);
    if (menu) {
        menu.classList.toggle('hidden');
        console.log('Toggled - now hidden:', menu.classList.contains('hidden'));
    } else {
        console.log('ERROR: userMenu element not found');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const userMenu = document.getElementById('userMenu');
    const menuContainer = document.getElementById('userMenuContainer');
    
    // Only close if clicking outside the entire dropdown container
    if (userMenu && menuContainer && !menuContainer.contains(event.target)) {
        userMenu.classList.add('hidden');
    }
});

// Tab switching for posts feed
function showTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => {
        tab.classList.remove('show');
        tab.classList.add('hidden');
    });
    
    // Remove active class from all buttons
    const buttons = document.querySelectorAll('[id$="-tab"]');
    buttons.forEach(button => {
        button.classList.remove('border-blue-600', 'text-blue-600');
        button.classList.add('border-transparent', 'text-gray-600');
    });
    
    // Show selected tab
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.remove('hidden');
        selectedTab.classList.add('show');
    }
    
    // Activate selected button
    const selectedButton = document.getElementById(tabName + '-tab');
    if (selectedButton) {
        selectedButton.classList.remove('border-transparent', 'text-gray-600');
        selectedButton.classList.add('border-blue-600', 'text-blue-600');
    }
}
