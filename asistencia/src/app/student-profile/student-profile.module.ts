import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';

import { StudentProfilePageRoutingModule } from './student-profile-routing.module';
import { StudentProfilePage } from './student-profile.page';
import { ZXingScannerModule } from '@zxing/ngx-scanner'; // Importa el módulo del escáner de QR

@NgModule({
  imports: [
    CommonModule,                  // Funcionalidades comunes de Angular
    FormsModule,                   // Para trabajar con formularios
    IonicModule,                   // Funcionalidades de Ionic
    StudentProfilePageRoutingModule, // Rutas específicas de esta página
    ZXingScannerModule             // Módulo necesario para el escáner de QR
  ],
  declarations: [StudentProfilePage] // Declara el componente StudentProfilePage
})
export class StudentProfilePageModule {}
