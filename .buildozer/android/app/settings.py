class Settings():
    def __init__(self):
        self.screen_width=980
        self.screen_height=540
        self.bgr_color=(207,151,215)
        
        self.bullet_allowed=5
        self.ship_limit=2
        #bullet settings
        
        self.bullet_width=30
        self.bullet_height=15
        self.bullet_color=255,20,147
        #allien settings
        
        self.fleet_drop_speed=10

        self.speedup_scale=1.1
        self.speedup_bullet=5
        self.score_scale=1.2
        self.initize_dynamic_settings()
    def initize_dynamic_settings(self):
        self.speed_factor=1
        self.bullet_speed_factor=1.5

        self.allien_speed_factor=0.5
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction=1
        #scoring 
        self.allien_point=50
        self.pause=False
        

    def increase_speed(self):
        self.speed_factor *=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.allien_speed_factor*=self.speedup_scale
        self.bullet_width +=self.speedup_bullet
        self.allien_point= int(self.allien_point* self.score_scale)
        # print(self.allien_point)

    

        
