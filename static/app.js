// Fonctions utilitaires pour l'interface
function formatDate(date) {
    return new Date(date).toLocaleString('fr-FR');
}

// Gestion des notifications
const notifications = {
    show(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification fixed top-4 right-4 p-4 rounded-lg shadow-lg ${type === 'error' ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`;
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
};

// Formatage des priorités
function getPriorityClass(priority) {
    switch(priority.toUpperCase()) {
        case 'HIGH':
            return 'high';
        case 'MEDIUM':
            return 'medium';
        case 'LOW':
            return 'low';
        default:
            return 'medium';
    }
}

// Mise à jour automatique des données
function setupAutoRefresh(callback, interval = 5000) {
    setInterval(callback, interval);
}
