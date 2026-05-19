package api

import (
	"encoding/json"
	"net/http"
)

// HealthCheck verifica que la API está funcionando
func HealthCheck(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{
		"status":  "ok",
		"message": "Servidor de Chat funcionando correctamente",
	})
}