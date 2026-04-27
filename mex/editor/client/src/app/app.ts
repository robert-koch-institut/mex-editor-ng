import { AsyncPipe } from "@angular/common";
import { HttpClient } from "@angular/common/http";
import { Component, inject, signal } from "@angular/core";
import { MatButton } from "@angular/material/button";
import { MatIcon } from "@angular/material/icon";
import { MatSlideToggle } from "@angular/material/slide-toggle";
import { RouterLink, RouterOutlet } from "@angular/router";

interface PreviewItem {
  identifier: string;
  $type: string;
}

interface PaginatedPreviewItems {
  items: PreviewItem[];
  total: number;
}

@Component({
  selector: "app-root",
  imports: [
    RouterOutlet,
    RouterLink,
    AsyncPipe,
    MatButton,
    MatIcon,
    MatSlideToggle,
  ],
  templateUrl: "./app.html",
  styleUrl: "./app.scss",
})
export class App {
  protected readonly title = signal("mex-editor-ng");

  private http = inject(HttpClient);

  data$ = this.http.get<PaginatedPreviewItems>("api/v0/backend/preview-item");

  onClick() {
    console.warn("CLICKED");
  }
}
