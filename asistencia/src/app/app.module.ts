import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'; // Importar CUSTOM_ELEMENTS_SCHEMA
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { HttpClientModule } from '@angular/common/http';
import { QRCodeModule } from 'angularx-qrcode'; // Para generar QR, si lo necesitas
import { ZXingScannerModule } from '@zxing/ngx-scanner'; // Importamos el escáner QR

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [AppComponent], // Componentes declarados en la app principal
  imports: [
    BrowserModule,
    IonicModule.forRoot(), // Inicialización de Ionic
    AppRoutingModule,
    HttpClientModule, // Para consumo de APIs
    QRCodeModule, // Módulo opcional para generar códigos QR
    ZXingScannerModule // Módulo necesario para el escáner QR
  ],
  providers: [
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy } // Estrategia de rutas en Ionic
  ],
  bootstrap: [AppComponent], // Componente raíz de la aplicación
  schemas: [CUSTOM_ELEMENTS_SCHEMA] // Permite usar elementos personalizados como <zxing-scanner>
})
export class AppModule {}
