package main

import (
	"fmt"
	"log"
	"net/http"

	// Ajusta esta ruta a la de tu módulo si cambiaste el nombre en el 'go mod init'
	"github.com/tu-usuario/chat-go-project/internal/api" 
)

func main() {
	// Definición de Endpoints iniciales
	http.HandleFunc("/api/v1/health", api.HealthCheck)

	// Placeholder para el futuro endpoint de WebSockets
	http.HandleFunc("/ws/chat", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Endpoint de WebSockets en construcción para la Etapa 3")
	})

	puerto := ":8080"
	fmt.Printf("🚀 Servidor iniciado en http://localhost%s\n", puerto)
	
	// Arranca el servidor
	if err := http.ListenAndServe(puerto, nil); err != nil {
		log.Fatalf("Error al arrancar el servidor: %v", err)
	}
}