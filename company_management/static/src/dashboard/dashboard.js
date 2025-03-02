import { Component, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { View } from "@web/views/view";


class RobotiaDashboard extends Component {
  static template = "company_management.robotia_dashboard";
  static components = { View }
  setup() {
    super.setup()
    this.menuService = useService('menu')
    this.orm = useService('orm')
    this.actionService = useService('action')
    this.clickAction = {}
    onWillStart(async () => {
      const searchViewId = await this.orm.call(
        "robotia.company",
        "get_default_dashboard_search_view_id",
        []
      );

      this.clickAction = await this.orm.call(
        "robotia.company",
        "get_default_dashboard_company"
      );

      this.getListCompanyViewProps = {
        resModel: "robotia.company",
        type: "list",
        showButtons: false,
        noBreadcrumbs: true,
        searchViewId: searchViewId,
        limit: 10
      };
    })
  }

  getApps() {
    // chỉ lấy ra 8 app (theo đề bài)
    return this.menuService.getApps().slice(0, 8)
  }
  
  onClickApp(app) {
    this.actionService.doAction(this.clickAction)
  }
}

registry.category("actions").add("robotia_dashboard", RobotiaDashboard);