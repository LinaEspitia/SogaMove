document.addEventListener('DOMContentLoaded', () => {
    const commentsList = document.getElementById('comments-list');
    const postButton = document.getElementById('post-comment');
    const commentInput = document.querySelector('#new-comment textarea');

    // Función para cargar comentarios
    async function loadComments() {
        try {
            const response = await fetch('/comments');
            const comments = await response.json();

            // Limpiar la lista
            commentsList.innerHTML = '';

            // Agregar cada comentario
            comments.forEach(comment => {
                const commentElement = document.createElement('div');
                commentElement.className = 'comment';
                commentElement.innerHTML = `
                    <div class="comment-header">
                        <span class="username">${comment.username}</span>
                        <span class="time">${new Date(comment.timestamp).toLocaleString()}</span>
                    </div>
                    <div class="comment-body">
                        <p>${comment.content}</p>
                    </div>
                `;
                commentsList.appendChild(commentElement);
            });
        } catch (error) {
            console.error('Error al cargar comentarios:', error);
        }
    }

    // Función para publicar un nuevo comentario
    postButton.addEventListener('click', async () => {
        const content = commentInput.value.trim();
        if (!content) {
            alert('El comentario no puede estar vacío.');
            return;
        }

        try {
            const response = await fetch('/comments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: 1, // Reemplazar con el ID del usuario autenticado
                    content: content,
                }),
            });

            if (response.ok) {
                commentInput.value = '';
                await loadComments();
            } else {
                const error = await response.json();
                alert(`Error: ${error.error}`);
            }
        } catch (error) {
            console.error('Error al publicar comentario:', error);
        }
    });

    // Cargar comentarios al inicio
    loadComments();
});
