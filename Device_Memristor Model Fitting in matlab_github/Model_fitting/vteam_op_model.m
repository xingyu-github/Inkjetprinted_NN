%% VTEAM Model (Negative voltage perform OFF switching)
% Without window function !

function [v,i,x] = vteam_op_model(v_input,t_vec,x_init,iv,input_parameters)


%Fill parameters here
%-----------------------
Roff    = 3500;
Ron     = 225;
%voff    = input_parameters(5);%Must be negative; 
%von     = input_parameters(6);%Must be positive;
% koff    =(10^-5)*input_parameters(1);
% aoff    =input_parameters(2);
koff    =-3.8731e-9;
aoff    =0.9064;
voff    = -0.01;%Must be negative; 
kon     =(10^-5)*input_parameters(1);
aon     =input_parameters(2);
von     = 0.02;%Must be positive;
% kon     =2.9513e-9;
% aon     =1.2577;

P_coeff = 2;


D       =  1e-7;% Device length 
xoff    = 0;
xon     = D;
%-----------------------

i=zeros(length(t_vec),1);

v=v_input;
lambda=reallog(Ron/Roff);
% 
% for j=1:length(t_vec)
%     if j==1
%         x(j)=x_init;
%         if iv==0
%             i(j)=v(j)/(Roff+((Ron-Roff)/(xon-xoff))*(x(j)-xoff));
%         elseif iv==1
%             i(j)=v(j)/(Roff*exp(lambda*(x(j)-xoff)/(xon-xoff)));
%         end
%     else 
%         dt=t_vec(j)-t_vec(j-1);
%         if v(j)<=voff
%             dxdt(j)=(koff*((v(j)/voff-1))^aoff);
%             x(j)=x(j-1)+dxdt(j)*dt;
%         elseif v(j)>=von
%             dxdt(j)=(kon*((v(j)/von)-1)^aon);
%             x(j)=x(j-1)+dxdt(j)*dt;
%         else
%             dxdt(j)=0;
%             x(j)=x(j-1);
%         end
% 
%         if (x(j)<0)
%             x(j)=0;
%             dxdt(j)=0;
%         elseif (x(j) > D) 
%             x(j)=D;
%             dxdt(j)=0;
%         end
%     
%         if iv==0
%             i(j)=v(j)/(Roff+((Ron-Roff)/(xon-xoff))*(x(j)-xoff));
%         elseif iv==1
%             i(j)=v(j)/(Roff*exp(lambda*(x(j)-xoff)/(xon-xoff)));
%         end
%     end
% end
% 
% end
% 

%use Biolek window function
for j=1:length(t_vec)
    if j==1
        x(j)=x_init;
        if iv==0
            i(j)=v(j)/(Roff+((Ron-Roff)/(xon-xoff))*(x(j)-xoff));
        elseif iv==1
            i(j)=v(j)/(Roff*exp(lambda*(x(j)-xoff)/(xon-xoff)));
        end
    else 
        dt=t_vec(j)-t_vec(j-1);
        if v(j)<=voff
            dxdt(j)=(koff*((v(j)/voff-1))^aoff);
            x(j)=x(j-1)+dxdt(j)*dt.*(1-(1-x(j-1)/D-heaviside(v(j)))^(2*P_coeff));
        elseif v(j)>=von
            dxdt(j)=(kon*((v(j)/von)-1)^aon);
            x(j)=x(j-1)+dxdt(j)*dt.*(1-(1-x(j-1)/D-heaviside(v(j)))^(2*P_coeff));
        else
            dxdt(j)=0;
            x(j)=x(j-1);
        end

        if (x(j)<0)
            x(j)=0;
            dxdt(j)=0;
        elseif (x(j) > D) 
            x(j)=D;
            dxdt(j)=0;
        end
    
        if iv==0
            i(j)=v(j)/(Roff+((Ron-Roff)/(xon-xoff))*(x(j)-xoff));
        elseif iv==1
            i(j)=v(j)/(Roff*exp(lambda*(x(j)-xoff)/(xon-xoff)));
        end
    end
end

end



