import { AsyncPipe } from "@angular/common";
import { HttpClient } from "@angular/common/http";
import { Component, inject, signal } from "@angular/core";

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
    AsyncPipe,
  ],
  templateUrl: "./app.html",
  styleUrl: "./app.scss",
})
export class App {
  protected readonly title = signal("mex-editor-ng");
  private http = inject(HttpClient);

  data$ = this.http.get<PaginatedPreviewItems>("api/v0/backend/preview-item");
}
