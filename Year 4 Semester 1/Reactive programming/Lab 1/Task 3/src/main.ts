import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/module';
import "./secrets"

const platform = platformBrowserDynamic();
platform.bootstrapModule(AppModule);