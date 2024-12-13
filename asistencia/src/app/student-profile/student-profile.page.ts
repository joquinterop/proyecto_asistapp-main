import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ConsumoapiService } from '../service/consumoapi.service'; 
import { ToastController, AlertController } from '@ionic/angular';  
import { BarcodeFormat } from '@zxing/browser';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.page.html',
  styleUrls: ['./student-profile.page.scss'],
})
export class StudentProfilePage implements OnInit {
  // Variables del perfil del estudiante
  nombre: string | undefined;
  receivedId: number | undefined;
  fotoPerfil: string | undefined;
  correo: string | undefined;

  // Variables para el escaneo QR
  qrResultString: string | null = null;

  // Formatos aceptados para el escaneo
  formats: BarcodeFormat[] = [BarcodeFormat.QR_CODE];

  constructor(
    private router: Router,
    private consumoAPI: ConsumoapiService, 
    private toastController: ToastController,
    private alertController: AlertController  
  ) {}

  ngOnInit() {
    // Configurar datos iniciales
    if (history.state) {
      this.nombre = history.state.nombre;
      this.receivedId = history.state.id;
      this.fotoPerfil = history.state.fotoPerfil;
      this.correo = history.state.correo;
    }
  }

  // Método que se ejecuta cuando se escanea un código QR
  onCodeResult(resultString: string) {
    this.qrResultString = resultString;

    try {
      // Procesar los datos del QR
      const qrData = JSON.parse(resultString);
      const cursoId = qrData.curso_id;
      const asignatura = qrData.asignatura;
      const fecha = qrData.fecha;
      const alumnoId = this.receivedId;

      if (alumnoId !== undefined && cursoId) {
        this.consumoAPI.obtenerProfesorPorCurso(cursoId).subscribe(
          (profesorData: any) => {
            const profesorId = profesorData.profesor_id;
            this.consumoAPI.actualizarAsistencia(profesorId, cursoId, alumnoId).subscribe(
              async () => {
                const toast = await this.toastController.create({
                  message: `Asistencia confirmada en ${asignatura} el día ${fecha}`,
                  duration: 3000,
                  position: 'middle',
                  color: 'success'
                });
                await toast.present();
              },
              (error) => console.error('Error al actualizar asistencia:', error)
            );
          },
          (error) => {
            console.error('Error al obtener el ID del profesor:', error);
          }
        );
      } else {
        console.error('ID de alumno o datos del QR no definidos');
      }
    } catch (error) {
      console.error('Error al procesar el QR:', error);
    }
  }

  // Método para cerrar sesión
  async cerrarSesion() {
    const alert = await this.alertController.create({
      header: 'Confirmar cierre de sesión',
      message: '¿Estás seguro de que deseas cerrar sesión?',
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          handler: () => {
            console.log('Cierre de sesión cancelado');
          }
        },
        {
          text: 'Cerrar sesión',
          handler: () => {
            localStorage.clear(); 
            this.router.navigate(['/login']);  
          }
        }
      ]
    });

    await alert.present();
  }
}
