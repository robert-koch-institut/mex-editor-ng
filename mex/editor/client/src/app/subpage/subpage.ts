import { Component, inject } from "@angular/core";
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: "app-subpage",
  imports: [],
  templateUrl: "./subpage.html",
  styleUrl: "./subpage.scss",
})
export class Subpage {
  private activatedRoute = inject(ActivatedRoute);
  title = this.activatedRoute.snapshot.data["title"] || "WHY...";
}
