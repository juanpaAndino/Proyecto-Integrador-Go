package models

import "time"

// User representa el modelo de base de datos para los usuarios
type User struct {
	ID           string    `json:"id"`
	Username     string    `json:"username"`
	Email        string    `json:"email"`
	PasswordHash string    `json:"-"` // El guion evita que la contraseña se envíe en el JSON
	CreatedAt    time.Time `json:"created_at"`
}